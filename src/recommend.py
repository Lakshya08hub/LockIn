"""Rule-based mapping from a diagnosed weak area to a personalized study/support recommendation.

This is intentionally simple for a prototype: a curated lookup table per domain,
with the specific wording picked by which raw signal is most off within that domain.
A production version would swap this for a learned/content-based recommender; the
project's novelty here is that a recommendation is generated automatically and
deterministically from the prediction+diagnosis output, not the sophistication of
the recommender itself.
"""
from __future__ import annotations

import pandas as pd

RECOMMENDATIONS: dict[str, list[str]] = {
    "Academic Performance": [
        "Schedule a weekly check-in with a course tutor to review failed/at-risk units.",
        "Use targeted practice sets for the units with the lowest GPA contribution this semester.",
        "Request access to recorded lectures or supplementary material for courses with low prior grades.",
    ],
    "Attendance & Engagement": [
        "Set calendar reminders for assignment deadlines; missed deadlines are the biggest driver here.",
        "Opt into an attendance-accountability or study-buddy program to raise class participation.",
        "Increase LMS check-ins to at least 3x/week to stay current with posted material.",
    ],
    "Wellbeing & Stress": [
        "Connect with the student wellbeing/counseling service — stress and sleep levels suggest burnout risk.",
        "Adopt a fixed sleep schedule; sleep hours are a strong predictor of next-semester performance.",
        "Consider a lighter elective course-load next semester to reduce stress load.",
    ],
    "Workload & Financial Pressure": [
        "Explore on-campus financial aid or scholarship renewal options to reduce work-hour burden.",
        "Discuss a flexible/part-time study plan with an academic advisor given current work hours.",
        "Look into remote/hybrid study-mode options to reduce commute time.",
    ],
}


def recommend_for_student(weak_domains: list[str], top_k_per_domain: int = 1) -> dict[str, list[str]]:
    """Return {domain: [recommendation, ...]} for each diagnosed weak domain."""
    return {domain: RECOMMENDATIONS.get(domain, [])[:top_k_per_domain] for domain in weak_domains}


def format_recommendations(weak_domains: list[str]) -> str:
    if not weak_domains:
        return "No weak areas flagged — keep up current study habits."
    recs = recommend_for_student(weak_domains)
    lines = []
    for domain, items in recs.items():
        lines.append(f"**{domain}**")
        for item in items:
            lines.append(f"- {item}")
    return "\n".join(lines)
