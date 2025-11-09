# 📉 Customer Churn Prediction Using Machine Learning 🚀  

Welcome to the **Customer Churn Prediction System** — an end-to-end machine learning project designed to predict whether a customer is likely to leave (churn) or stay based on their demographic and service usage data.  

This project showcases the full machine learning lifecycle — from **data preprocessing and exploratory analysis to model training, optimization, and deployment** using **FastAPI**.  

---

## 📚 Project Overview  

The goal of this project is to analyze telecom customer data and build a machine learning model that predicts churn behavior.  
By identifying at-risk customers, telecom providers can proactively take retention measures.  

The project workflow includes:  

- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Feature Engineering  
- Model Training and Evaluation  
- Model Export & Deployment with FastAPI  

---

## 🧩 Technologies Used  

- **Python 3.9+**  
- **FastAPI** – for API development  
- **Scikit-learn** – for model training and tuning  
- **Pandas & NumPy** – for data manipulation  
- **Matplotlib & Seaborn** – for data visualization  
- **Joblib** – for model persistence  
- **Jupyter Notebook** – for experimentation and analysis  

---

## 📂 Project Structure  

```
Customer Churn Prediction/
│
├── Customer_Churn.csv                      # Dataset
├── Customer Churn Prediction.ipynb         # Jupyter Notebook (EDA + Model Training)
├── customer_churn_app.py                   # FastAPI Web App
├── model.pkl                               # Final Trained Model
├── scaler.pkl                              # StandardScaler for normalization
├── Customer Churn Prediction.pdf           # Project Report
└── README.md                               # Documentation
```

---

## 🧠 Machine Learning Pipeline  

### 1️⃣ Data Cleaning & Preprocessing  
- Verified no missing or duplicate records.  
- Encoded `Gender`: Female → 1, Male → 0.  
- Encoded target variable `Churn`: Yes → 1, No → 0.  
- Selected input features:  
  `['Age', 'Gender', 'Tenure', 'MonthlyCharges']`  

---

### 2️⃣ Exploratory Data Analysis (EDA)  
Visualized trends using **Seaborn** and **Matplotlib**:  
- Churn distribution (Yes/No)  
- Monthly charges vs. churn rate  
- Average tenure of churned vs. retained customers  
- Contract type and Internet Service impact  

**Key Insights:**  
- Customers with **Month-to-Month** contracts had higher churn rates.  
- Customers using **Fiber Optic** services were more prone to churn.  
- **Shorter tenure** and **higher monthly charges** correlated with churn.  

---

### 3️⃣ Feature Engineering  
- Standardized numerical features using **StandardScaler**.  
- Encoded categorical data (Gender, Contract Type, Internet Service).  
- Split dataset into train and test sets (80/20).  

---

### 4️⃣ Model Training & Evaluation  

Multiple classification models were trained and optimized using **GridSearchCV**:  

| Model | Description | Accuracy |
|--------|--------------|-----------|
| Logistic Regression | Linear classifier | **88%** |
| K-Nearest Neighbors | Distance-based learner | 88% |
| Support Vector Machine (SVM) | Linear Kernel | **89%** |
| Decision Tree | Rule-based classifier | 80.5% |
| Random Forest | Ensemble learning | 88.5% |

The **SVM model** achieved the best performance and was selected as the final model.  

```python
joblib.dump(gridsvm.best_estimator_, 'model.pkl')
```

---

## ⚙️ API Deployment (FastAPI)  

### **Endpoint**
`POST /predict/`

---

### **Request Body (JSON)**
```json
{
  "Age": 35,
  "Gender": 1,
  "Tenure": 12,
  "MonthlyCharges": 65.5
}
```

---

### **Response Example**
```json
{
  "prediction": "Customer will Churn"
}
```

---

### **Run the FastAPI App**
```bash
uvicorn customer_churn_app:app --reload
```

Then open:  
👉 **http://127.0.0.1:8000/docs**  
to access and test the interactive Swagger UI.

---

## 📈 Model Results  

- **Algorithm:** Support Vector Machine (SVM)  
- **Accuracy:** 89%  
- **Evaluation:** Tuned via GridSearchCV (kernel = linear, C = 0.01)  
- **Use Case:** Predicting customer churn likelihood for telecom services  

---

## 💾 Saved Artifacts  

- **model.pkl** – Trained SVM model  
- **scaler.pkl** – Scaler used for normalization  
- **Customer Churn Prediction.ipynb** – Model training notebook  
- **customer_churn_app.py** – FastAPI deployment file  

---

## 🚀 Future Enhancements  

- Integrate **Deep Learning** models (ANN or XGBoost).  
- Implement **real-time churn prediction pipeline** with Kafka/Spark.  
- Add **database support** (PostgreSQL / MongoDB).  
- Develop an **interactive dashboard** with Streamlit or Power BI.  
