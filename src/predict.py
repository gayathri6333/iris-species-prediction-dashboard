import argparse
from joblib import load
import numpy as np
from pathlib import Path

def load_model(path: str = "models/model.joblib"):
    if not Path(path).exists():
        raise FileNotFoundError(f"Model not found at {path}. Run: python src/train.py")
    return load(path)

def main():
    parser = argparse.ArgumentParser(description="Predict Iris species from 4 features.")
    parser.add_argument("--features", "-f", nargs=4, type=float, required=True,
                        metavar=("SEPAL_LEN","SEPAL_WID","PETAL_LEN","PETAL_WID"),
                        help="Four numeric features in order.")
    args = parser.parse_args()

    model = load_model()
    X = np.array(args.features, dtype=float).reshape(1, -1)
    pred = model.predict(X)[0]
    proba = getattr(model, "predict_proba", lambda _: None)(X)
    target_names = ["setosa", "versicolor", "virginica"]
    print(f"Predicted class: {target_names[pred]}")
    if proba is not None:
        print("Class probabilities:", proba[0])

if __name__ == "__main__":
    main()
