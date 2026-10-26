"""Weak-area diagnosis.

The dataset has no per-subject marks, so "weak areas" are approximated as four
domains known from the literature to drive academic risk (see research_papers.md,
Cluster A/B). For each domain we build a composite score from the relevant raw
columns, z-score it against the training population, and flag a domain as a
weak area for a given student when their composite z-score falls in the bottom
quartile (configurable) of that domain -- i.e. this student is meaningfully
worse off than their peers in that specific dimension, not just overall.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

# Each domain: columns plus the direction in which a HIGHER raw value means
# WORSE standing (so we know whether to flip the z-score before comparing).
DOMAINS: dict[str, dict] = {
    "Academic Performance": {
        "higher_is_worse": ["units_failed"],
        "higher_is_better": ["gpa_semester_1", "gpa_semester_2", "admission_grade", "previous_qualification_grade"],
    },
    "Attendance & Engagement": {
        "higher_is_worse": ["missed_deadlines"],
        "higher_is_better": ["attendance_rate", "assignments_submitted_rate", "lms_logins_per_week", "library_visits_per_month"],
    },
    "Wellbeing & Stress": {
        "higher_is_worse": ["stress_level"],
        "higher_is_better": ["sleep_hours", "satisfaction_score", "mental_health_support"],
    },
    "Workload & Financial Pressure": {
        "higher_is_worse": ["weekly_work_hours", "commute_time_mins"],
        "higher_is_better": ["tuition_up_to_date"],
    },
}


def _zscore(series: pd.Series, mean: float, std: float) -> pd.Series:
    std = std if std > 1e-9 else 1.0
    return (series - mean) / std


def fit_domain_stats(df: pd.DataFrame) -> dict:
    """Compute per-column mean/std on the training population, used to score any student later."""
    stats = {}
    for col in [c for spec in DOMAINS.values() for c in (*spec["higher_is_worse"], *spec["higher_is_better"])]:
        stats[col] = (df[col].mean(), df[col].std())
    return stats


def score_domains(df: pd.DataFrame, stats: dict) -> pd.DataFrame:
    """Return one composite 'weakness score' per domain per student.

    Higher weakness score = worse standing in that domain. Scores are the mean
    of the (direction-adjusted) z-scores of that domain's columns.
    """
    out = pd.DataFrame(index=df.index)
    for domain, spec in DOMAINS.items():
        parts = []
        for col in spec["higher_is_worse"]:
            mean, std = stats[col]
            parts.append(_zscore(df[col], mean, std))  # higher raw -> higher weakness, no flip
        for col in spec["higher_is_better"]:
            mean, std = stats[col]
            parts.append(-_zscore(df[col], mean, std))  # higher raw -> lower weakness, flip
        out[domain] = np.mean(parts, axis=0)
    return out


def diagnose_weak_areas(domain_scores: pd.DataFrame, quantile_threshold: float = 0.75) -> pd.DataFrame:
    """Flag a domain as a weak area for a student when their weakness score is at/above
    the given quantile of that domain's weakness-score distribution (default: worst 25%)."""
    thresholds = domain_scores.quantile(quantile_threshold)
    flags = domain_scores.ge(thresholds)
    return flags


def weakest_domains_for_student(domain_scores_row: pd.Series, flags_row: pd.Series, top_n: int = 2) -> list[str]:
    flagged = flags_row[flags_row].index.tolist()
    if not flagged:
        return []
    ranked = domain_scores_row[flagged].sort_values(ascending=False)
    return ranked.index.tolist()[:top_n]
