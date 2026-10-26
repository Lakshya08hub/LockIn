# Kaggle Datasets — Student Academic Performance

> Compiled for: Final-year project on Academic Risk Prediction + Weak-Area Identification + Personalized Study Recommendation.
> Goal: identify datasets that improve on the standard **UCI Student Performance** dataset (Cortez & Silva — ~395–649 Portuguese secondary-school students, 2 schools, 30–33 features) on size, feature richness, and demographic/geographic scope. Licenses and freshness should be re-verified on Kaggle directly before use, as dataset pages update over time.

---

### 1. Student Academic Performance & Dropout Risk
- **Link:** https://www.kaggle.com/datasets/mohankrishnathalla/student-academic-performance-and-dropout-risk
- **Size:** ~100,000 rows × 32 engineered features
- **Key features:** Academic records, engagement/behavioral metrics, dropout-risk labels, course type, study mode, nationality field
- **Geographic/demographic scope:** 15 nationalities, 5 course types, 3 study modes — explicitly multi-demographic
- **Suitability: High** — By far the best match for the project's stated novelty (large scale + multi-demographic + risk-labeled). Large enough for robust DT/RF/LR training and subgroup validation. Verify whether it is fully synthetic/semi-synthetic vs. real-world sourced, and check feature documentation for engineering artifacts.

### 2. Student Exam Performance & Success Dataset
- **Link:** https://www.kaggle.com/datasets/mobeenfatimah/student-exam-performance-and-success-dataset
- **Size:** ~100,000 rows × 44 features
- **Key features:** Household income bracket, parental education, urban/rural location, study habits, attendance, pass/fail and exam-score targets
- **Geographic/demographic scope:** Socioeconomic + urban/rural split; no explicit country field
- **Suitability: High** — Largest feature set found (44 columns), strong socioeconomic coverage addresses the "limited features" drawback directly. Semi-synthetic — good for model development, but synthetic generation process should be disclosed/caveated in the methodology section.

### 3. College Students Academic Performance Dataset
- **Link:** https://www.kaggle.com/datasets/zara2099/college-students-academic-performance-dataset
- **Size:** ~7,000 rows × 25 columns
- **Key features:** Attendance, learning behavior, academic-risk indicators — explicitly designed for "prediction, classification, and intervention planning"
- **Geographic/demographic scope:** Higher-education, single-region focus (scope not stated as multi-country)
- **Suitability: High** — Purpose-built for exactly this project's use case (intervention planning), moderate size is good for a student project's compute/timeline. Best "realistic middle ground" choice if the 100K datasets feel too synthetic.

### 4. Students Performance Dataset (rabieelkharoua)
- **Link:** https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset
- **Size:** Mid-size (exact row count to confirm on page), grade-class target variable
- **Key features:** Parental support, study habits, extracurricular activity, ages 15–18
- **Geographic/demographic scope:** Age-banded, parental-support variable adds socioeconomic proxy; single-context
- **Suitability: Medium** — Good feature diversity but smaller/less documented scope than #1–#3. Useful as a secondary/validation dataset for cross-dataset generalization testing (strengthens the "limited scope" rebuttal in the proposal).

### 5. Student Performance and Learning Behavior Dataset
- **Link:** https://www.kaggle.com/datasets/adilshamim8/student-performance-and-learning-style
- **Size:** 14,003 rows × 16 attributes (merged from two public Kaggle datasets)
- **Key features:** ExamScore and FinalGrade targets, learning-style/behavior attributes; CC BY 4.0 licensed
- **Geographic/demographic scope:** Merged-source, moderate diversity; license is clean for academic reuse
- **Suitability: Medium–High** — Good size, explicit learning-behavior angle supports weak-area/study-style analysis, and the permissive license is a practical plus for a thesis appendix/reproducibility.

### 6. Student Performance Dataset: Academic Insights 10K
- **Link:** https://www.kaggle.com/datasets/nadeemajeedch/students-performance-10000-clean-data-eda
- **Size:** ~10,000 rows
- **Key features:** Demographics including lunch-type (free/reduced lunch as socioeconomic proxy), pre-cleaned for EDA
- **Geographic/demographic scope:** Socioeconomic proxy present; no country/region field confirmed
- **Suitability: Medium** — Convenient size (matches typical academic-project compute budgets) and pre-cleaned, but feature depth is lower than #1/#2. Good as a fast-iteration/prototyping dataset before scaling up to the 100K sets.

### 7. Student Performance Factors Dataset
- **Link:** https://www.kaggle.com/datasets/mosapabdelghany/student-performance-factors-dataset
- **Size:** To confirm on page (typically mid-size, feature-rich "factors" style dataset)
- **Key features:** Multiple behavioral/environmental factor columns (study time, sleep, parental involvement, etc. — typical of this dataset family)
- **Geographic/demographic scope:** Not clearly multi-region; verify on page
- **Suitability: Medium** — Useful as a supplementary feature-engineering reference; confirm size/scope before committing it as a primary dataset.

### 8. UCI-sourced Portuguese Math/Language Sets (via arXiv 2407.13112, hosted copies also on Kaggle)
- **Link (paper referencing the data):** https://arxiv.org/pdf/2407.13112
- **Size:** Math: 395 rows; Portuguese language: 649 rows (the original UCI benchmark)
- **Key features:** 30–33 features including study time, failures, family background, final grade G3
- **Geographic/demographic scope:** 2 Portuguese schools only — this is the baseline being improved upon, included here for direct comparison
- **Suitability: Low (as primary dataset) / High (as benchmark for comparison)** — Include this explicitly as the "baseline" dataset in the methodology to quantitatively demonstrate the project's improvement in scale and scope versus datasets #1–#6.

---

## Comparison Table

| Dataset | Rows | Features | Demographic/Geo Scope | Socioeconomic Data | Suitability |
|---|---|---|---|---|---|
| Student Academic Performance & Dropout Risk | ~100,000 | 32 | 15 nationalities, 5 course types | Yes | **High** |
| Student Exam Performance & Success | ~100,000 | 44 | Urban/rural, income, parental edu | Yes (rich) | **High** |
| College Students Academic Performance | ~7,000 | 25 | Higher-ed, single region | Partial | **High** |
| Students Performance (rabieelkharoua) | Mid | ~10+ | Age-banded, single context | Partial | Medium |
| Student Performance & Learning Behavior | 14,003 | 16 | Merged-source | Partial | Medium–High |
| Academic Insights 10K | 10,000 | ~10 | Lunch-type proxy | Partial | Medium |
| Student Performance Factors | Mid (TBD) | TBD | Unclear | Partial | Medium |
| UCI Portuguese Math/Language (baseline) | 395 / 649 | 30–33 | 2 schools, 1 country | No | Low (use as baseline only) |

---

## Recommendations
- **Primary training dataset:** *Student Academic Performance & Dropout Risk* (100K rows, 15 nationalities) — best addresses the "small/limited scope" drawback at scale.
- **Secondary/feature-depth dataset:** *Student Exam Performance & Success Dataset* (44 features, rich socioeconomic fields) — best for feature-engineering the "weak-area" dimensions (per-subject/per-skill scores if present) and the recommendation layer's input features.
- **Validation/generalization dataset:** *College Students Academic Performance* or *Student Performance & Learning Behavior* — use as an out-of-distribution test set to demonstrate the model generalizes beyond a single data source.
- **Baseline comparison:** UCI Portuguese dataset (395/649 rows) — explicitly benchmark against this to quantify the scale/scope improvement claimed as the project's novelty.
- **Caveat to document in the proposal:** several large "100K" datasets are synthetic or semi-synthetic. This should be disclosed transparently — synthetic data solves the *sample-size* drawback but does not fully solve the *real-world validity* drawback. Consider blending a real dataset (UCI, or #3/#5) with a large synthetic one, or explicitly scoping the project as "ML pipeline development + synthetic-at-scale validation, with real-data case study."

---

*Sources:*
- [Student Performance Prediction Dataset (prajwalkanade)](https://www.kaggle.com/datasets/prajwalkanade/student-performance-prediction-dataset)
- [Student Performance Prediction (amrmaree)](https://www.kaggle.com/datasets/amrmaree/student-performance-prediction)
- [Student performance prediction (rkiattisak)](https://www.kaggle.com/datasets/rkiattisak/student-performance-in-mathematics)
- [Student Performance (Multiple Linear Regression)](https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression)
- [College Students Academic Performance Dataset](https://www.kaggle.com/datasets/zara2099/college-students-academic-performance-dataset)
- [Students Performance Dataset (rabieelkharoua)](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)
- [Student Exam Performance & Success Dataset](https://www.kaggle.com/datasets/mobeenfatimah/student-exam-performance-and-success-dataset)
- [Student Performance and Learning Behavior Dataset](https://www.kaggle.com/datasets/adilshamim8/student-performance-and-learning-style)
- [Improvement of Applicability in Student Performance Prediction Based on Transfer Learning (arXiv, references UCI sets)](https://arxiv.org/pdf/2407.13112)
- [Student Academic Performance & Dropout Risk](https://www.kaggle.com/datasets/mohankrishnathalla/student-academic-performance-and-dropout-risk)
- [Student Performance Dataset: Academic Insights 10K](https://www.kaggle.com/datasets/nadeemajeedch/students-performance-10000-clean-data-eda)
- [Student Performance (neuralsorcerer)](https://www.kaggle.com/datasets/neuralsorcerer/student-performance)
- [Student Performance Factors Dataset](https://www.kaggle.com/datasets/mosapabdelghany/student-performance-factors-dataset)
