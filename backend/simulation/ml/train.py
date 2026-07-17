from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parent

DATASET_PATH = BASE_DIR / "collision_dataset.csv"

MODEL_PATH = BASE_DIR / "model.pkl"


def train():

    print("Loading dataset...")

    df = pd.read_csv(DATASET_PATH)

    X = df.drop(columns=["collision_risk"])

    y = df["collision_risk"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y,
    )

    print(f"Training samples : {len(X_train)}")
    print(f"Testing samples  : {len(X_test)}")

    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        min_samples_split=8,
        min_samples_leaf=4,
        random_state=42,
        n_jobs=-1,
    )

    print("\nTraining model...")

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    probabilities = model.predict_proba(X_test)[:, 1]

    print("\n==============================")
    print("MODEL EVALUATION")
    print("==============================")

    print(
        f"Accuracy : {accuracy_score(y_test, predictions):.4f}"
    )

    print(
        f"ROC-AUC  : {roc_auc_score(y_test, probabilities):.4f}"
    )

    print("\nConfusion Matrix")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report")
    print(classification_report(y_test, predictions))

    print("\nFeature Importance")

    for feature, importance in sorted(
        zip(X.columns, model.feature_importances_),
        key=lambda x: x[1],
        reverse=True,
    ):
        print(
            f"{feature:<30} {importance:.4f}"
        )

    joblib.dump(model, MODEL_PATH)

    print(
        f"\nModel saved to:\n{MODEL_PATH}"
    )


if __name__ == "__main__":
    train()