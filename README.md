# Python Projects
# Machine Learning Projects Portfolio

This repository showcases machine learning projects, each solving a real-world business problem with data-driven solutions. All models are built using Python and deployed via Streamlit for interactive use.

---

## 🚀 Tech Stack
- Python (Pandas, Scikit-learn, Seaborn, Matplotlib)
- Streamlit for UI
- FastAPI
- Joblib for model serialization
- GridSearchCV for hyperparameter tuning
  
---
## 📁 1. Customer Churn Prediction

Predicts whether a telecom customer will churn based on demographic and service usage patterns.

### 🔹 Dataset
- Features: Age, Gender, Tenure, MonthlyCharges, Contract Type, Internet Service
- Target: Churn (Yes/No)

### 🔹 Workflow
- EDA with visualizations
- Preprocessing: encoding, scaling
- Models: Logistic Regression, KNN, SVM (best), Decision Tree, Random Forest
- SVM achieved best accuracy of **89%**
- Deployment: Streamlit app (`customer_churn_app.py`)

### 🔹 Run the App
```bash
pip install -r requirements.txt
streamlit run customer_churn_app.py
```

---

## 📁 2. Fraud Detection Using ML and Web App

Detects fraudulent financial transactions using behavioral and balance-based features.

### 🔹 Dataset
- 6.3M+ transactions with type, amount, balances, and fraud labels

### 🔹 Workflow
- Feature engineering (balance differences)
- Preprocessing with `ColumnTransformer` and encoding
- Model: Logistic Regression with class balancing
- Achieved **95% accuracy**, high recall for fraud cases
- Deployment: Streamlit app (`fraud_detection_app.py`)

### 🔹 Run the App
```bash
pip install -r requirements.txt
streamlit run fraud_detection_app.py
```

---

## 📁 3. Loan Approval Prediction System

Predicts whether a loan application will be approved using applicant income, education, credit history, and other features.

### 🔹 Dataset
- 308 clean records with categorical and numerical variables

### 🔹 Workflow
- Visual exploration of approval rates by demographics
- Feature encoding and scaling
- Models: Logistic Regression (best), KNN, SVM
- Best accuracy: **84.9%**
- Deployment-ready model using `joblib` for web app integration

### 🔹 Run the App
```bash
pip install -r requirements.txt
streamlit run loan_approval_app.py
```


---

## 📁 4. Bank Churn Classification

Predicts whether a customer will subscribe to a term deposit based on demographic and marketing campaign data.

### 🔹 Dataset
- Features include: age, job, marital status, balance, campaign, previous outcome
- Target: `deposit` (Yes/No)

### 🔹 Workflow
- Visual EDA using histograms, heatmaps, and skewness metrics
- Feature correlation and skewness correction
- Models likely applied: Logistic Regression or Tree-based (based on similar pattern)

### 🔹 Libraries Used
- Pandas, Seaborn, Scikit-learn, SciPy

> _Note: Notebook includes deep statistical visualizations and exploratory techniques._

---

## 📁 5. Cancer Classification

Classifies tumors as malignant or benign using a dataset of 30+ biological features.

### 🔹 Dataset
- Source: `cancer_classification.csv`
- No missing values
- Target: binary classification (Malignant or Benign)

### 🔹 Workflow
- EDA: Missing value heatmaps, distribution plots, skewness checks
- Model training (likely Logistic Regression, SVM, or Neural Network)
- Evaluation via confusion matrix, accuracy, F1-score

### 🔹 Libraries Used
- Pandas, Matplotlib, Seaborn, SciPy, Scikit-learn

## 📬 Contact
For any inquiries or collaboration opportunities, feel free to reach out via [LinkedIn](https://www.linkedin.com/in/kotechadhruv/).
