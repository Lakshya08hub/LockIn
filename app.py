"""Streamlit prototype: Student Academic Risk & Weak-Area Recommendation.

Run: streamlit run app.py
"""
from pathlib import Path

import joblib
import pandas as pd
import streamlit as st

from src.data_loader import BINARY_COLS, CATEGORICAL_COLS, ID_COL, NUMERIC_COLS, TARGET_COL, load_data
from src.weak_areas import DOMAINS, score_domains, weakest_domains_for_student
from src.recommend import format_recommendations
from src.train_models import train_and_evaluate

st.set_page_config(page_title="LockIn — Student Risk & Recommendation", layout="wide")

MODELS_DIR = "models"
FEATURE_COLS = CATEGORICAL_COLS + BINARY_COLS + NUMERIC_COLS


@st.cache_data
def load_full_data():
    return load_data()


@st.cache_resource
def load_artifacts(_df: pd.DataFrame):
    """Load pre-built models from models/ if present (fast local path). Otherwise
    (e.g. a fresh deploy where the large joblib files aren't checked into git) train
    them in-memory once and cache the result for the lifetime of this app instance."""
    required = [
        f"{MODELS_DIR}/decision_tree.joblib",
        f"{MODELS_DIR}/random_forest.joblib",
        f"{MODELS_DIR}/logistic_regression.joblib",
        f"{MODELS_DIR}/metrics_comparison.csv",
        f"{MODELS_DIR}/domain_stats.joblib",
        f"{MODELS_DIR}/best_model.txt",
    ]
    if all(Path(p).exists() for p in required):
        models = {
            "Decision Tree": joblib.load(f"{MODELS_DIR}/decision_tree.joblib"),
            "Random Forest": joblib.load(f"{MODELS_DIR}/random_forest.joblib"),
            "Logistic Regression": joblib.load(f"{MODELS_DIR}/logistic_regression.joblib"),
        }
        metrics = pd.read_csv(f"{MODELS_DIR}/metrics_comparison.csv", index_col=0)
        domain_stats = joblib.load(f"{MODELS_DIR}/domain_stats.joblib")
        with open(f"{MODELS_DIR}/best_model.txt") as f:
            best_model_key = f.read().strip()
        return models, metrics, domain_stats, best_model_key

    with st.spinner("First-time setup: training models on this deployment (~1 min)…"):
        out = train_and_evaluate(_df)
    label_map = {"decision_tree": "Decision Tree", "random_forest": "Random Forest", "logistic_regression": "Logistic Regression"}
    models = {label_map[k]: v for k, v in out["pipelines"].items()}
    return models, out["metrics_df"], out["domain_stats"], out["best_model"]


df = load_full_data()
models, metrics, domain_stats, best_model_key = load_artifacts(df)


@st.cache_data
def population_domain_thresholds(_domain_stats):
    full_domain_scores = score_domains(df[FEATURE_COLS], _domain_stats)
    return full_domain_scores.quantile(0.75)


domain_thresholds = population_domain_thresholds(domain_stats)

key_to_label = {
    "decision_tree": "Decision Tree",
    "random_forest": "Random Forest",
    "logistic_regression": "Logistic Regression",
}

st.title("🎓 LockIn — Student Academic Risk & Personalized Recommendation")
st.caption(
    "Predicts dropout/academic risk, diagnoses weak areas across four domains, "
    "and generates a personalized recommendation per weak area."
)

with st.expander("Model comparison (Decision Tree / Random Forest / Logistic Regression)", expanded=False):
    st.dataframe(metrics.style.highlight_max(axis=0, color="#1f6f3f"))
    st.caption(f"Best model by F1-score: **{key_to_label[best_model_key]}**")

st.divider()

mode = st.radio("Choose input mode", ["Pick an existing student by ID", "Enter a new student manually"], horizontal=True)

if mode == "Pick an existing student by ID":
    student_id = st.number_input("Student (person_id)", min_value=int(df[ID_COL].min()), max_value=int(df[ID_COL].max()), value=int(df[ID_COL].min()))
    row = df[df[ID_COL] == student_id]
    if row.empty:
        st.error("No student with that ID.")
        st.stop()
    input_row = row[FEATURE_COLS].iloc[0]
    actual_dropout = row[TARGET_COL].iloc[0]
    st.info(f"Actual recorded outcome for this student — dropout: **{'Yes' if actual_dropout else 'No'}** (for reference only, not used in prediction)")
else:
    st.subheader("Enter student details")
    cols = st.columns(3)
    values = {}
    with cols[0]:
        values["gender"] = st.selectbox("Gender", sorted(df["gender"].unique()))
        values["nationality"] = st.selectbox("Nationality", sorted(df["nationality"].unique()))
        values["family_income_level"] = st.selectbox("Family income level", sorted(df["family_income_level"].unique()))
        values["course_type"] = st.selectbox("Course type", sorted(df["course_type"].unique()))
        values["study_mode"] = st.selectbox("Study mode", sorted(df["study_mode"].unique()))
        values["age"] = st.slider("Age", 17, 60, 21)
        values["semester"] = st.slider("Semester", 1, 12, 3)
    with cols[1]:
        values["admission_grade"] = st.slider("Admission grade", 0.0, 200.0, 140.0)
        values["previous_qualification_grade"] = st.slider("Previous qualification grade", 0.0, 200.0, 140.0)
        values["units_enrolled"] = st.slider("Units enrolled", 1, 20, 10)
        values["units_passed"] = st.slider("Units passed", 0, 20, 8)
        values["units_failed"] = st.slider("Units failed", 0, 20, 1)
        values["gpa_semester_1"] = st.slider("GPA semester 1", 0.0, 4.0, 3.0)
        values["gpa_semester_2"] = st.slider("GPA semester 2", 0.0, 4.0, 3.0)
    with cols[2]:
        values["attendance_rate"] = st.slider("Attendance rate (%)", 0.0, 100.0, 85.0)
        values["assignments_submitted_rate"] = st.slider("Assignments submitted rate (%)", 0.0, 100.0, 85.0)
        values["library_visits_per_month"] = st.slider("Library visits/month", 0, 30, 4)
        values["lms_logins_per_week"] = st.slider("LMS logins/week", 0.0, 50.0, 10.0)
        values["missed_deadlines"] = st.slider("Missed deadlines", 0, 20, 1)
        values["stress_level"] = st.slider("Stress level (1-10)", 1, 10, 5)
        values["sleep_hours"] = st.slider("Sleep hours/night", 0.0, 12.0, 7.0)

    cols2 = st.columns(4)
    with cols2[0]:
        values["first_generation"] = int(st.checkbox("First-generation student"))
    with cols2[1]:
        values["disability_status"] = int(st.checkbox("Disability status"))
    with cols2[2]:
        values["scholarship_holder"] = int(st.checkbox("Scholarship holder"))
    with cols2[3]:
        values["tuition_up_to_date"] = int(st.checkbox("Tuition up to date", value=True))

    cols3 = st.columns(4)
    with cols3[0]:
        values["part_time_job"] = int(st.checkbox("Has part-time job"))
    with cols3[1]:
        values["international_student"] = int(st.checkbox("International student"))
    with cols3[2]:
        values["extracurricular_activities"] = int(st.checkbox("Extracurricular activities"))
    with cols3[3]:
        values["mental_health_support"] = int(st.checkbox("Using mental health support"))

    values["weekly_work_hours"] = st.slider("Weekly work hours", 0, 60, 0)
    values["commute_time_mins"] = st.slider("Commute time (mins)", 0, 180, 20)
    values["satisfaction_score"] = st.slider("Satisfaction score (1-10)", 1, 10, 7)

    input_row = pd.Series(values)[FEATURE_COLS]

st.divider()

model_choice = st.selectbox("Model to use for risk prediction", list(models.keys()), index=list(models.keys()).index(key_to_label[best_model_key]))
pipe = models[model_choice]

input_df = pd.DataFrame([input_row])
risk_proba = pipe.predict_proba(input_df)[0, 1]
risk_label = "HIGH RISK" if risk_proba >= 0.5 else "LOW RISK"

col_a, col_b = st.columns([1, 2])
with col_a:
    st.metric("Predicted dropout risk probability", f"{risk_proba:.1%}")
    st.markdown(f"### {'🔴' if risk_label == 'HIGH RISK' else '🟢'} {risk_label}")

with col_b:
    domain_scores = score_domains(input_df, domain_stats)
    thresholds = domain_thresholds
    flags_row = (domain_scores.iloc[0] >= thresholds)
    weak_domains = weakest_domains_for_student(domain_scores.iloc[0], flags_row, top_n=4)

    st.subheader("Diagnosed weak area(s)")
    if weak_domains:
        for d in weak_domains:
            st.write(f"- **{d}** (weakness score: {domain_scores.iloc[0][d]:.2f}, population 75th pct: {thresholds[d]:.2f})")
    else:
        st.write("No domain flagged below the risk threshold.")

st.divider()
st.subheader("Personalized recommendations")
st.markdown(format_recommendations(weak_domains))

with st.expander("Domain definitions (what drives each weak-area score)"):
    for domain, spec in DOMAINS.items():
        st.markdown(f"**{domain}**: {', '.join(spec['higher_is_worse'] + spec['higher_is_better'])}")
