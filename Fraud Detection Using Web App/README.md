# 💳 Fraud Detection Using Machine Learning and Web App

Welcome to the **Fraud Detection Using Machine Learning and Web App** — a complete end-to-end data science project that identifies fraudulent financial transactions using machine learning and deploys the model through a web interface built with **FastAPI**.

This project demonstrates **data preprocessing, feature engineering, exploratory analysis, and ML model deployment** to detect fraud in financial transactions effectively.

---

## 📚 Project Overview

The objective of this project is to detect fraudulent transactions from a financial dataset using **machine learning**.
It includes all stages of the data science workflow:

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Training and Evaluation
- Model Serialization
- Deployment through FastAPI Web Application

The web app allows users to input transaction details and instantly check whether the transaction is **fraudulent** or **legitimate**.

---

## 🧩 Technologies Used

- **Python 3.9+**
- **FastAPI** – API development framework
- **Scikit-learn** – for ML modeling
- **Pandas & NumPy** – data handling and manipulation
- **Matplotlib & Seaborn** – data visualization
- **Joblib** – model persistence
- **Jupyter Notebook** – for interactive analysis and development

---

## 📂 Project Structure

```
Fraud Detection Using ML and Web App/
├── image.png                          # 👈 your screenshot file
├── fraud_detection_app.py
├── fraud_detection_pipeline.pkl
├── Fraud Detection Using ML and Web App.ipynb
├── README.md                          # 👈 this file


```

---

## 🧠 Machine Learning Pipeline

### 1️⃣ Data Cleaning & Preprocessing
- Removed unnecessary columns (`step`, `nameOrig`, `nameDest`, etc.)
- Added new derived features:
  - `balanceDiffOrigi = oldbalanceOrg - newbalanceOrig`
  - `balanceDiffDest = newbalanceDest - oldbalanceDest`
- Ensured data consistency and handled negative balances

---

### 2️⃣ Exploratory Data Analysis (EDA)
Visualized transaction patterns using **Seaborn** and **Matplotlib**:
- Distribution of transaction types
- Fraud rate by transaction type
- Top senders and receivers
- Correlation matrix of numerical features

Key finding:
> Fraudulent transactions are primarily of type **TRANSFER** and **CASH_OUT**.

---

### 3️⃣ Feature Engineering
Selected key features for modeling:
`['type', 'amount', 'oldbalanceOrg', 'newbalanceOrig', 'oldbalanceDest', 'newbalanceDest', 'balanceDiffOrigi', 'balanceDiffDest']`

- Applied **OneHotEncoding** for categorical data (`type`)
- Scaled numerical features using **StandardScaler**

---

### 4️⃣ Model Training
Used **Logistic Regression** with balanced class weights to handle imbalanced data.
Implemented with a **Pipeline** for preprocessing and model training in one step.

**Performance Summary:**

| Metric | Non-Fraud (0) | Fraud (1) |
|---------|----------------|-----------|
| Precision | 1.00 | 0.02 |
| Recall | 0.95 | 0.94 |
| F1-Score | 0.97 | 0.04 |
| Accuracy | **95%** |

---

### 5️⃣ Model Export
Serialized the trained pipeline:
```python
import joblib
joblib.dump(pipeline, 'fraud_detection_pipeline.pkl')
```

---

## ⚙️ API Deployment (FastAPI)

### **Endpoint**
`POST /predict/`

---

### **Request Body (JSON)**
```json
{
  "type": "TRANSFER",
  "amount": 50000.0,
  "oldbalanceOrg": 100000.0,
  "newbalanceOrig": 50000.0,
  "oldbalanceDest": 0.0,
  "newbalanceDest": 50000.0
}
```

---

### **Response Example**
```json
{
  "prediction": "Fraudulent Transaction"
}
```

---

### **Run the FastAPI App**
```bash
uvicorn fraud_detection_app:app --reload
```

Then open:
👉 **http://127.0.0.1:8000/docs**
to interact with the Swagger UI and test predictions.

---

## 📈 Model Results

- **Algorithm:** Logistic Regression
- **Evaluation:** Classification Report & Confusion Matrix
- **Accuracy:** ~95%
- **Best Use Case:** Detecting potential fraudulent transactions in real-time banking systems

---

## 🚀 Future Enhancements

- Integrate **deep learning** models (e.g., LSTM, Autoencoders) for anomaly detection
- Implement **real-time fraud detection pipeline** using streaming tools (Kafka, Spark)
- Add **database integration** (PostgreSQL / MongoDB)
- Build a **frontend dashboard** using Streamlit or React for visualization
