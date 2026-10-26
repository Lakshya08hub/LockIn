"""Train and compare Decision Tree, Random Forest, and Logistic Regression on the
dropout-risk target. Saves each fitted pipeline plus a metrics comparison table.

Run: python -m src.train_models
"""
from __future__ import annotations

import json
from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from src.data_loader import BINARY_COLS, CATEGORICAL_COLS, NUMERIC_COLS, TARGET_COL, load_data
from src.weak_areas import fit_domain_stats

MODELS_DIR = Path(__file__).resolve().parent.parent / "models"
MODELS_DIR.mkdir(exist_ok=True)

FEATURE_COLS = CATEGORICAL_COLS + BINARY_COLS + NUMERIC_COLS


def build_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL_COLS),
            ("num", StandardScaler(), NUMERIC_COLS + BINARY_COLS),
        ]
    )


def get_models() -> dict:
    return {
        "decision_tree": DecisionTreeClassifier(max_depth=8, random_state=42, class_weight="balanced"),
        "random_forest": RandomForestClassifier(n_estimators=300, max_depth=12, random_state=42, class_weight="balanced", n_jobs=-1),
        "logistic_regression": LogisticRegression(max_iter=2000, class_weight="balanced"),
    }


def evaluate(y_true, y_pred, y_proba) -> dict:
    return {
        "accuracy": round(accuracy_score(y_true, y_pred), 4),
        "precision": round(precision_score(y_true, y_pred), 4),
        "recall": round(recall_score(y_true, y_pred), 4),
        "f1": round(f1_score(y_true, y_pred), 4),
        "roc_auc": round(roc_auc_score(y_true, y_proba), 4),
    }


def train_and_evaluate(df: pd.DataFrame) -> dict:
    """Train all three models on the given dataframe and return everything the app needs,
    without touching disk. Used both by main() (which then persists to models/) and by
    app.py as a cold-start fallback on deployments where models/ isn't pre-built (e.g.
    Streamlit Community Cloud, where the 99MB random_forest.joblib isn't checked into git)."""
    X = df[FEATURE_COLS]
    y = df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    pipelines = {}
    results = {}
    for name, clf in get_models().items():
        pipe = Pipeline(steps=[("prep", build_preprocessor()), ("clf", clf)])
        pipe.fit(X_train, y_train)

        y_pred = pipe.predict(X_test)
        y_proba = pipe.predict_proba(X_test)[:, 1]
        metrics = evaluate(y_test, y_pred, y_proba)
        results[name] = metrics
        pipelines[name] = pipe

    domain_stats = fit_domain_stats(X_train.join(y_train).drop(columns=[TARGET_COL]))
    best_model = max(results, key=lambda k: results[k]["f1"])
    metrics_df = pd.DataFrame(results).T

    return {
        "pipelines": pipelines,
        "metrics": results,
        "metrics_df": metrics_df,
        "domain_stats": domain_stats,
        "best_model": best_model,
    }


def main():
    df = load_data()
    out = train_and_evaluate(df)

    for name, pipe in out["pipelines"].items():
        joblib.dump(pipe, MODELS_DIR / f"{name}.joblib")
        print(f"{name}: {out['metrics'][name]}")

    with open(MODELS_DIR / "metrics.json", "w") as f:
        json.dump(out["metrics"], f, indent=2)

    joblib.dump(out["domain_stats"], MODELS_DIR / "domain_stats.joblib")

    with open(MODELS_DIR / "best_model.txt", "w") as f:
        f.write(out["best_model"])
    print(f"\nBest model by F1: {out['best_model']}")

    out["metrics_df"].to_csv(MODELS_DIR / "metrics_comparison.csv")
    print("\n" + out["metrics_df"].to_string())


if __name__ == "__main__":
    main()
