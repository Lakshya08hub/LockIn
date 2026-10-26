"""Load and lightly validate the student dropout-risk dataset."""
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "student_dropout_risk_2026.csv"

TARGET_COL = "dropout"
ID_COL = "person_id"

CATEGORICAL_COLS = [
    "gender", "nationality", "family_income_level", "course_type", "study_mode",
]

BINARY_COLS = [
    "first_generation", "disability_status", "scholarship_holder", "tuition_up_to_date",
    "part_time_job", "international_student", "extracurricular_activities",
    "mental_health_support",
]

NUMERIC_COLS = [
    "age", "weekly_work_hours", "semester", "admission_grade", "previous_qualification_grade",
    "units_enrolled", "units_passed", "units_failed", "gpa_semester_1", "gpa_semester_2",
    "attendance_rate", "assignments_submitted_rate", "library_visits_per_month",
    "lms_logins_per_week", "missed_deadlines", "stress_level", "satisfaction_score",
    "commute_time_mins", "sleep_hours",
]


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = set([TARGET_COL, ID_COL, *CATEGORICAL_COLS, *BINARY_COLS, *NUMERIC_COLS]) - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing expected columns: {sorted(missing)}")
    return df
