# Project Report: Iris Flower Classification (AI with Python)

**Name:** _Your Name_  
**Internship:** GradGuru — AI with Python  
**Date:** _YYYY‑MM‑DD_

## 1. Introduction
This project predicts the Iris flower species (Setosa, Versicolor, Virginica) from 4 numeric features.
It demonstrates a full ML workflow: data loading, training, evaluation, and deployment via a small web app.

## 2. Dataset
- Source: `sklearn.datasets.load_iris()` (no external download needed)
- Instances: 150
- Features: 4 (all numeric)
- Classes: 3 species

## 3. Methodology
- Split: Train/Test split (stratified)
- Model: Scikit‑learn `Pipeline(StandardScaler(), LogisticRegression)`
- Metrics: accuracy, confusion matrix, classification report

## 4. Results
After running `python src/train.py`, the following artifacts are generated:
- `reports/metrics.json` — include accuracy here.
- `reports/classification_report.txt` — precision/recall/F1 per class.
- `reports/confusion_matrix.png` — paste into your submission.

_Add your brief analysis here (e.g., which classes are harder to distinguish, any bias/variance observations)._
You may mention typical accuracy is high (>90%) on Iris with linear models, but report your actual number.

## 5. Inference / App
The `app_streamlit.py` provides a slider-based UI for predictions.
Include one or two screenshots of the app with different inputs and outputs.

## 6. Conclusion
- Summarize performance.
- Mention potential improvements: hyperparameter tuning, trying SVM/RandomForest, cross‑validation, feature importance, etc.

## 7. References
- Scikit‑learn documentation
- Original Iris dataset (Fisher, 1936)

