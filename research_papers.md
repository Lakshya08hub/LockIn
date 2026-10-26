# Research Papers — Student Academic Performance Prediction, Weak-Area Diagnosis & Personalized Recommendation

> Compiled for: Final-year project on Academic Risk Prediction + Weak-Area Identification + Personalized Study Recommendation
> Scope note: Papers are grouped into three clusters matching the project's pipeline — (A) performance/risk prediction, (B) weak-area/skill diagnosis (knowledge tracing), (C) personalized recommendation. Drawback tags use the codes: **[SD]** Small Dataset, **[LS]** Limited Scope (demographic/geographic), **[LF]** Limited Features, **[NR]** No Recommendations (prediction-only).

---

## Cluster A — Academic Performance / At-Risk Prediction

### 1. Student Performance Prediction Using Machine Learning Algorithms
- **Authors & Year:** Ahmed et al., 2024
- **Venue:** *Applied Computational Intelligence and Soft Computing* (Wiley), DOI: 10.1155/2024/4067721
- **Summary:** Compares multiple ML classifiers (including Random Forest, Decision Tree, Logistic Regression-family models) on a student dataset to predict final academic outcomes. Reports Random Forest as a strong performer among benchmarked algorithms.
- **Drawbacks present:** **[NR]** — pure grade/outcome prediction, no downstream recommendation step. **[LS]** — single-institution style data, scope not generalized across regions.
- **Relevance to proposed novelty:** Good baseline for the ML comparison section (DT/RF/LR benchmarking) of the project; demonstrates the exact algorithm family specified in the project brief, but stops exactly where this project's novelty begins (no recommendation layer).

### 2. Machine Learning Approaches for Early Student Performance Prediction in Programming Education
- **Authors & Year:** 2025
- **Venue:** *Information* (MDPI), DOI: 10.3390/info17010060
- **Summary:** Uses multi-modal student data (midterm grades, lab completion times, engagement logs) in a university programming course to predict final exam performance. XGBoost achieved >84% accuracy; midterm grade and lab completion duration were most predictive. Frames the predictor as a feeder for an "intelligent recommender system" for at-risk students, though the recommender itself is only proposed, not built.
- **Drawbacks present:** **[LS]** — single course/institution. **[NR]** — recommendation framed conceptually but not implemented/evaluated.
- **Relevance:** Strong evidence for feature selection (behavioral + continuous-assessment features outperform static demographics) and for motivating the "prediction → recommendation" pipeline this project aims to close.

### 3. Empirical Review of Student Performance Prediction Models
- **Authors & Year:** 2024
- **Venue:** *Computer Engineering and Intelligent Systems* (empirical review/survey)
- **Summary:** Benchmarks five ML algorithms for performance prediction; Random Forest Classifier achieves the best accuracy (85.42%). Explicitly flags lack of standardized evaluation metrics across studies, limited model generalizability, and potential bias in training data as field-wide problems.
- **Drawbacks present:** **[LS]**, **[SD]** — the review itself critiques the field for these issues, making it a useful citation for the "research drawbacks" section of the project proposal rather than a technical baseline.
- **Relevance:** Directly supports the project's problem statement — this paper's own stated limitations ARE the gap the project is targeting. Cite when justifying the novelty argument.

### 4. Predictive Analytics in Gamified Education: A Hybrid Model for Identifying At-Risk Students
- **Authors & Year:** 2025
- **Venue:** PMC (PMC12369421)
- **Summary:** Builds a hybrid of Logistic Regression, Decision Tree, and Random Forest to detect at-risk students in a gamified learning environment; the hybrid model outperforms any single classifier, enabling earlier intervention flags.
- **Drawbacks present:** **[NR]** — stops at risk-flagging, no personalized study-resource output. **[LS]** — gamified/single-platform context.
- **Relevance:** Directly validates the project's proposed ML stack (DT + RF + LR ensemble/hybrid) as a sound architecture for the prediction stage; useful methodological template.

### 5. Logistic Regression and Random Forest Comparison in Predicting Students' Qualification Based on Half-Semester Performance
- **Authors & Year:** 2023
- **Venue:** ResearchGate (preprint/conference)
- **Summary:** Direct head-to-head of Logistic Regression vs. Random Forest on half-semester performance data. LR: 70.8% accuracy / 40.4% precision / 97.0% recall; RF: 74.7% accuracy. Shows the classic precision-recall trade-off between the two algorithms.
- **Drawbacks present:** **[SD]**, **[LF]** — half-semester institutional data only, narrow feature set.
- **Relevance:** Useful citation for justifying *why* the project benchmarks multiple algorithms rather than committing to one — performance is dataset-dependent, so a comparative approach (as the project proposes) is methodologically correct.

### 6. Analysis and Prediction of At-Risk Students Using Machine Learning Algorithms
- **Authors & Year:** 2024/2025
- **Venue:** arXiv preprint
- **Summary:** Logistic Regression and Linear-Kernel SVM reportedly reach ~99% accuracy identifying at-risk students (treat this figure cautiously — likely an artifact of class imbalance, data leakage, or a narrow test set, a common issue in this literature).
- **Drawbacks present:** **[SD]** likely, **[NR]**. Also serves as a cautionary example of over-optimistic reported accuracy from a non-representative/small dataset.
- **Relevance:** Useful as a critical-discussion citation — the project write-up can use this to argue why larger, more diverse datasets (its own stated improvement) are necessary to produce trustworthy risk scores instead of inflated accuracy figures.

### 7. Identifying At-Risk K-12 Students in Multimodal Online Environments: A Machine Learning Approach
- **Authors & Year:** 2020 (arXiv 2003.09670)
- **Venue:** arXiv
- **Summary:** Uses multimodal online-learning behavioral data (not just grades) to flag K-12 at-risk students, broadening the feature space beyond demographics/marks.
- **Drawbacks present:** **[LS]** — single online platform, K-12 only.
- **Relevance:** Supports the project's "limited features" critique of prior work and shows precedent for incorporating behavioral/engagement features (which the project can add to differentiate from UCI-only approaches).

### 8. Evaluating the Student Performance Prediction and Action Framework Through a Learning Analytics Intervention Study
- **Authors & Year:** 2024
- **Venue:** *Education and Information Technologies* (Springer), DOI: 10.1007/s10639-024-12923-5
- **Summary:** Goes further than most of the literature — ML-identified at-risk students received **weekly personalized visual feedback and written recommendations** derived from LMS log data (engagement, motivation, retention signals), and the intervention's real-world effect was evaluated.
- **Drawbacks present:** Largely **addresses** the "no recommendation" drawback (this is one of the few papers that closes the loop) but is **[LS]** — single institution/LMS, and feedback was manually templated rather than an automated per-student weak-area + resource recommender.
- **Relevance:** **This is the closest existing analog to the project's proposed novelty.** It is the single most important paper to build on / differentiate from: the project should (a) cite it as proof the "prediction + actionable feedback" loop improves outcomes, and (b) position its own contribution as automating and scaling that manual feedback loop via ML-driven weak-area tagging + resource recommendation, rather than templated LMS messages.

---

## Cluster B — Weak-Area / Skill-Level Diagnosis (Knowledge Tracing)

### 9. DK-PRACTICE: An Intelligent Platform for Knowledge Tracing and Educational Content Recommendation
- **Authors & Year:** 2025
- **Venue:** Preprints.org (manuscript 202512.2641)
- **Summary:** Uses a Paired-Bipolar Bag-of-Words model to estimate per-student knowledge states from pre-/post-tests, then recommends content targeted at the detected gaps. Piloted with 98 second-year higher-education students.
- **Drawbacks present:** **[SD]** — n=98 is small. **[LS]** — single institution/cohort.
- **Relevance:** **Directly on-topic for "weak-area identification + recommendation."** This is the strongest methodological template for the diagnosis half of the project's novelty claim, but its tiny sample is exactly the "small/limited dataset" drawback the project proposal explicitly aims to fix — making it a good contrast citation ("DK-PRACTICE demonstrates feasibility on n=98; this project targets the same capability at a materially larger and more diverse scale").

### 10. A Survey of Explainable Knowledge Tracing
- **Authors & Year:** 2024
- **Venue:** arXiv (2403.07279)
- **Summary:** Surveys knowledge-tracing (KT) methods used to model per-concept student mastery, noting that KT-based systems are often not interpretable to educators/students, and reviews concept-tagged models (e.g., DKVMN) plus KT + reinforcement learning for adaptive learning paths.
- **Drawbacks present:** N/A (survey) — but explicitly discusses interpretability as an open problem, which matters because the project's Decision Tree/Random Forest approach is comparatively **more interpretable** than deep KT models.
- **Relevance:** Use to justify the choice of classical, interpretable models (DT/RF/LR) over opaque deep-KT architectures — interpretability is valuable for an actionable "weak area" report a student or advisor can actually read and trust.

### 11. A Review of Data Mining in Personalized Education: Current Trends and Future Prospects
- **Authors & Year:** 2024
- **Venue:** arXiv (2402.17236)
- **Summary:** Broad survey of educational data mining for personalization, covering student modeling, performance prediction, and resource recommendation as separate, often-disconnected research threads.
- **Drawbacks present:** Survey-level — but explicitly observes the field's fragmentation (prediction research and recommendation research rarely combined), which is the core gap this project fills.
- **Relevance:** Excellent citation for the Introduction/Related Work section to establish that "prediction" and "recommendation" are usually studied in isolation — directly motivating the project's integrated pipeline.

---

## Cluster C — Personalized Learning Recommendation

### 12. A Comprehensive Exploration of Personalized Learning in Smart Education: From Student Modeling to Personalized Recommendations
- **Authors & Year:** 2024
- **Venue:** arXiv (2402.01666)
- **Summary:** End-to-end survey spanning student modeling through to recommendation generation in "smart education" systems, covering architectures that connect a learner model to a recommendation engine.
- **Drawbacks present:** Survey-level; notes most deployed systems are large-scale industrial/MOOC systems, not something replicable with a small academic project's resources — relevant for scoping expectations.
- **Relevance:** Use as the conceptual architecture reference: student model (= the project's risk/weak-area prediction output) feeding a recommendation engine (= the project's personalized study-resource layer).

### 13. FAIREDU: A Multiple Regression-Based Method for Enhancing Fairness in Machine Learning Models for Educational Applications
- **Authors & Year:** 2024
- **Venue:** arXiv (2410.06423)
- **Summary:** Addresses fairness/bias across demographic subgroups in educational ML predictions — directly relevant to the "limited demographic scope" drawback, since models trained on narrow populations can produce biased risk scores when deployed more broadly.
- **Drawbacks present:** Methodological fix for **[LS]**-type bias rather than suffering from it.
- **Relevance:** Strong citation if the project dataset includes multiple demographic groups — supports adding a fairness check/validation step across subgroups as part of the project's novelty/robustness claims.

---

## Summary Table

| # | Paper | Year | Cluster | Key Drawback(s) | Addresses Novelty? |
|---|-------|------|---------|------------------|---------------------|
| 1 | Student Performance Prediction Using ML Algorithms (Wiley) | 2024 | A | NR, LS | Baseline only |
| 2 | Early Prediction in Programming Education (MDPI) | 2025 | A | LS, NR | Proposes but doesn't build recommender |
| 3 | Empirical Review of Prediction Models | 2024 | A | LS, SD (field-wide) | Motivates gap |
| 4 | Hybrid Model for At-Risk Students (PMC) | 2025 | A | NR, LS | Validates DT+RF+LR stack |
| 5 | LR vs RF on Half-Semester Data | 2023 | A | SD, LF | Justifies multi-model comparison |
| 6 | At-Risk Prediction (arXiv, ~99% acc.) | 2024/25 | A | SD (likely), NR | Cautionary example |
| 7 | At-Risk K-12 Multimodal (arXiv) | 2020 | A | LS | Supports richer feature sets |
| 8 | **LA Intervention Framework (Springer)** | 2024 | A | LS only | **Closest precedent — partially closes the loop** |
| 9 | DK-PRACTICE (Knowledge Tracing) | 2025 | B | SD, LS | **Direct template for weak-area diagnosis** |
| 10 | Explainable KT Survey | 2024 | B | — | Justifies interpretable DT/RF choice |
| 11 | DM in Personalized Education Review | 2024 | B | — | Confirms prediction/recommendation are usually disconnected |
| 12 | Smart Education Personalization Survey | 2024 | C | Scale mismatch | Architectural reference |
| 13 | FAIREDU Fairness Method | 2024 | C | Fixes LS-bias | Supports fairness validation |

---

*Sources (search-derived, verify access/DOI before citing in final submission):*
- [A Comprehensive Exploration of Personalized Learning in Smart Education](https://arxiv.org/pdf/2402.01666)
- [Using Machine Learning to Predict Students' Academic Performance with a Personalized Learning Plan](https://www.researchgate.net/publication/390546010_Using_Machine_Learning_to_Predict_Students'_Academic_Performance_with_a_Personalized_Learning_Plan)
- [Privacy-Preserving Personalization in Education](https://arxiv.org/pdf/2509.10516)
- [Student Performance Prediction Using Machine Learning Algorithms (ResearchGate)](https://www.researchgate.net/publication/380264177_Student_Performance_Prediction_Using_Machine_Learning_Algorithms)
- [Predicting the Performance of Students Using Deep Ensemble Learning (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC11677974/)
- [Student Performance Prediction Using Machine Learning Algorithms (Wiley)](https://onlinelibrary.wiley.com/doi/10.1155/2024/4067721)
- [Machine Learning Approaches for Early Student Performance Prediction in Programming Education](https://doi.org/10.3390/info17010060)
- [Evaluating the student performance prediction and action framework through a learning analytics intervention study](https://link.springer.com/article/10.1007/s10639-024-12923-5)
- [Predictive Modeling of Student Performance (IJACSA)](https://thesai.org/Downloads/Volume15No7/Paper_23-Predictive_Modeling_of_Student_Performance.pdf)
- [Predictive analytics in gamified education: hybrid model for at-risk students](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12369421/)
- [Logistic Regression and Random Forest Comparison](https://www.researchgate.net/publication/374300985_Logistic_Regression_and_Random_Forest_Comparison_in_Predicting_Students'_Qualification_Based_on_Students'_Half-Semester_Performance)
- [Analysis and Prediction of At-Risk Students Using Machine Learning Algorithms (arXiv)](https://arxiv.org/pdf/2606.20617)
- [Identifying At-Risk K-12 Students in Multimodal Online Environments (arXiv)](https://arxiv.org/pdf/2003.09670)
- [TutorLLM: Customizing Learning Recommendations with Knowledge Tracing and RAG](https://arxiv.org/pdf/2502.15709)
- [DK-PRACTICE preprint](https://www.preprints.org/manuscript/202512.2641)
- [A Survey of Explainable Knowledge Tracing](https://arxiv.org/pdf/2403.07279)
- [A Review of Data Mining in Personalized Education](https://arxiv.org/pdf/2402.17236)
- [FAIREDU: Enhancing Fairness in ML Models for Educational Applications](https://arxiv.org/pdf/2410.06423)
