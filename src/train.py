import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from joblib import dump

def main(random_state: int = 42, test_size: float = 0.2):
    Path("models").mkdir(parents=True, exist_ok=True)
    Path("reports").mkdir(parents=True, exist_ok=True)

    # Load data
    iris = load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    # Pipeline
    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("clf", LogisticRegression(max_iter=1000, multi_class="auto"))
    ])

    # Train
    pipe.fit(X_train, y_train)

    # Evaluate
    y_pred = pipe.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=target_names)

    # Save model
    dump(pipe, "models/model.joblib")

    # Save text report
    with open("reports/classification_report.txt", "w", encoding="utf-8") as f:
        f.write(report)

    # Save metrics.json
    metrics = {
        "accuracy": acc,
        "test_size": test_size,
        "random_state": random_state,
        "classes": list(map(str, target_names))
    }
    with open("reports/metrics.json", "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2)

    # Plot and save confusion matrix
    fig = plt.figure(figsize=(5, 4))
    ax = fig.add_subplot(111)
    im = ax.imshow(cm, interpolation="nearest")
    ax.set_title("Confusion Matrix")
    tick_marks = np.arange(len(target_names))
    ax.set_xticks(tick_marks)
    ax.set_yticks(tick_marks)
    ax.set_xticklabels(target_names)
    ax.set_yticklabels(target_names)
    ax.set_xlabel("Predicted label")
    ax.set_ylabel("True label")

    # Annotate cells
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, cm[i, j], ha="center", va="center")

    fig.tight_layout()
    fig.savefig("reports/confusion_matrix.png", dpi=150)
    plt.close(fig)

    print(f"Training complete. Accuracy: {acc:.4f}")
    print("Artifacts written to models/ and reports/ folders.")

if __name__ == "__main__":
    main()
