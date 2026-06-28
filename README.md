# GradGuru AI with Python — Iris Flower Classifier (End‑to‑End)

A clean, **ready-to-run** ML project you can submit today. It uses the classic **Iris** dataset (bundled inside scikit‑learn),
trains a model, evaluates it, saves reports, and exposes a small **Streamlit** app for interactive predictions.

## 📌 Problem Statement
Build a classifier that predicts the species of an Iris flower from 4 features:
- sepal length
- sepal width
- petal length
- petal width

## 🎯 Learning Objectives
- Load a dataset and split train/test.
- Build an ML **Pipeline** (scaler + classifier).
- Evaluate with accuracy, confusion matrix, classification report.
- Save the trained model and metrics to disk.
- Serve predictions with a lightweight **Streamlit** UI.

## 🗂️ Project Structure
```
GradGuru_AI_Python_Project_Iris/
├── requirements.txt
├── README.md
├── REPORT_TEMPLATE.md
├── SUBMISSION_CHECKLIST.txt
├── app_streamlit.py
├── models/
├── reports/
│   ├── (filled after training)
└── src/
    ├── train.py
    ├── predict.py
    └── utils.py
```

## 🚀 Quickstart (5 steps)
```bash
# 1) (Optional but recommended) create a virtual env
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) Train the model (creates models/ and reports/ artifacts)
python src/train.py

# 4) Try a CLI prediction
python src/predict.py --features 5.1 3.5 1.4 0.2

# 5) Launch the Streamlit app
streamlit run app_streamlit.py
```

## 📈 What gets generated after training
- `models/model.joblib` – the trained pipeline.
- `reports/metrics.json` – accuracy and other summary metrics.
- `reports/classification_report.txt` – precision/recall/F1 per class.
- `reports/confusion_matrix.png` – saved matplotlib figure.

## 📝 Submitting Your Work
1. Fill **REPORT_TEMPLATE.md** using the generated metrics & plots (or keep as-is if your program graders accept auto-generated artifacts).
2. Include the **reports/** folder artifacts and a few screenshots of the Streamlit UI.
3. Add your name, date, and internship info.

---

**Built on:** Python 3.10+ and scikit‑learn  
**Author:** S.Gayathri Devi 
**Date:** 2025-08-31
