import mlflow
import mlflow.sklearn
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from typing import Tuple, Any

# ===================================================================
# Step 1: Load and prepare the data
# ===================================================================


def load_data() -> Tuple[pd.DataFrame, pd.Series]:
    """Loads the Iris dataset as a pandas DataFrame."""
    iris = load_iris(as_frame=True)
    df = iris.frame
    df.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width',
'target']
    X = df.drop(columns=["target"]).astype("float64")
    y = df["target"]
    return X, y

# ===================================================================
# Step 2: Train and log the model using cross-validation
# ===================================================================


def train_and_log_model(model: Any, model_name: str, X: pd.DataFrame,
y: pd.Series) -> Tuple[str, float, Any]:
    with mlflow.start_run(run_name=model_name):
        scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')
        mean_cv_accuracy = np.mean(scores)
        mlflow.log_params(model.get_params())
        mlflow.log_metric("cv_accuracy", mean_cv_accuracy)
        model.fit(X, y)
        os.makedirs("models", exist_ok=True)
        model_path = f"models/{model_name}.pkl"
        joblib.dump(model, model_path)
        input_example = X.head(1)
        registered_model_name = f"iris-classifier-{model_name.lower()}"
        mlflow.sklearn.log_model(
            sk_model=model,
            artifact_path="model",
            registered_model_name=registered_model_name,
            input_example=input_example
        )

        print(f"{model_name} logged with CV accuracy: {mean_cv_accuracy:.4f}")
        return model_name, mean_cv_accuracy, model


# ===================================================================
# Step 3: Main execution block
# ===================================================================


if __name__ == "__main__":
    X, y = load_data()
    results = []
    print("--- Training Logistic Regression ---")
    name1, score1, model1 = train_and_log_model(
        LogisticRegression(max_iter=200),
        "LogisticRegression",
        X, y)
    
    results.append((name1, score1, model1))
    print("\n--- Training Random Forest ---")                   
    name2, score2, model2 = train_and_log_model(
        RandomForestClassifier(n_estimators=100, random_state=42),
        "RandomForest",
        X, y)
    results.append((name2, score2, model2))
    # Determine best model
    best_model_name, best_score, best_model = max(results, key=lambda x: x[1])
    print("\n🏆 Best model based on CV accuracy:")
    print(f"{best_model_name} ({best_score:.4f})")
    # ✅ Save best model as 'best_model.pkl' for API
    best_model_path = "models/best_model.pkl"
    joblib.dump(best_model, best_model_path)
    print(f"Best model saved to: {best_model_path}")
