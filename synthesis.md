# Synthesis — Best Sources to Build On & the Project's Specific Gap

## Best paper(s) to build on
1. **[Primary] "Evaluating the student performance prediction and action framework through a learning analytics intervention study"** (Education and Information Technologies, 2024) — this is the closest existing precedent to the project's full pipeline: it predicts at-risk students *and* delivers personalized feedback/recommendations, then evaluates real-world impact. The project should position itself as **automating and scaling** this manual, templated feedback loop using ML-driven weak-area tagging (closing the gap this paper leaves open) rather than reinventing prediction from scratch.
2. **[Secondary] "DK-PRACTICE: An Intelligent Platform for Knowledge Tracing and Educational Content Recommendation"** (2025) — the best methodological template specifically for the **weak-area diagnosis** half of the novelty claim (per-topic knowledge-state estimation feeding targeted content). Its small sample (n=98) is exactly the limitation the project's larger dataset will address.
3. **[Supporting] "A Review of Data Mining in Personalized Education"** (arXiv 2402.17236, 2024) — cited to establish, in the Related Work section, that prediction research and recommendation research are usually studied as disconnected threads in the literature — this is the structural gap the project fills by combining them in one pipeline.

## Best dataset(s) to use
1. **Primary: "Student Academic Performance & Dropout Risk"** (Kaggle, ~100,000 rows, 32 features, 15 nationalities) — directly resolves the "small/limited demographic-geographic scope" drawback at scale.
2. **Secondary: "Student Exam Performance & Success Dataset"** (Kaggle, ~100,000 rows, 44 features, rich socioeconomic fields) — provides the feature depth needed to engineer per-subject/weak-area signals and recommendation-relevant inputs.
3. **Baseline for comparison: UCI Portuguese Student Performance set** (395/649 rows, 2 schools) — retained only as a quantitative baseline to demonstrate scale/scope improvement, not as the primary training set.

## The specific gap this project fills
Existing literature splits cleanly into two camps that rarely intersect:
- **Prediction-only systems** (Cluster A papers) achieve good accuracy on academic risk but stop at a score or risk flag, with no actionable next step for the student (**[NR]** drawback).
- **Knowledge-tracing/recommendation systems** (Cluster B/C papers) diagnose weak areas or recommend content, but are typically validated on small, single-institution samples (**[SD]**/**[LS]** drawback) and are rarely demographically diverse.

The one paper that attempts the full loop (Springer 2024, LA intervention study) does so with **manually templated** feedback rather than an automated, ML-driven weak-area-to-resource mapping, and is still scoped to a single institution.

**This project's contribution** is therefore: a single pipeline — Decision Tree / Random Forest / Logistic Regression risk & weak-area prediction, trained on a materially larger and more demographically/geographically diverse dataset than prior work, that outputs not just a risk score but an **automated, personalized study-resource recommendation** per identified weak area — closing the prediction→recommendation gap at a scale and diversity existing studies have not demonstrated together.
