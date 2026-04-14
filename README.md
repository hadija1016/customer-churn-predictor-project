Customer Churn Prediction (Telco Dataset)
Overview

This project analyzes and predicts customer churn using the Telco Customer Churn dataset. It combines Exploratory Data Analysis (EDA) with machine learning models to identify high-risk customers and generate actionable business insights.

Dataset Information
Total customers: 7,043
Overall churn rate: 26.5%
Problem type: Binary Classification (Churn / No Churn)
Project Structure
CUSTOMER-CHURN-PREDICTION/
│
├── classification-models/
│   ├── models/
│   ├── notebooks/
│   │   ├── preprocessing.ipynb
│   │   ├── model-training.ipynb
│   │   ├── evaluation.ipynb
│   ├── outputs/
│
├── data/
│
├── Exploratory-data-analysis/
│   ├── notebooks/
│   │   ├── data_cleaning.ipynb
│   │   ├── eda_chart.ipynb
│   │   ├── insights_summary.ipynb
│   ├── outputs/
│   ├── reports/
│
├── shared/
├── requirement/
│
├── .gitignore
├── README.md
├── requirement.txt.txt
Exploratory Data Analysis Highlights
Churn rate: 26.5% of customers churned
High-risk segment: Month-to-month contracts (~43% churn)
Tenure impact: Customers in first 12 months show highest churn (~47%)
Pricing: Churned customers pay higher monthly charges (~$74 vs ~$61)
Services: Lack of online security significantly increases churn
Payment method: Electronic check users have the highest churn (~45%)
Models Used
Logistic Regression
Decision Tree
Random Forest
Workflow
Data Cleaning
Exploratory Data Analysis
Feature Engineering & Preprocessing
Model Training
Evaluation
Key Insights
Contract type is the strongest predictor of churn
Early-stage customers (0–12 months) are most vulnerable
Value-added services reduce churn probability
Payment behavior strongly correlates with churn
Business Recommendations
Encourage long-term contracts
Improve onboarding experience for new customers
Promote auto-pay over electronic checks
Bundle value-added services
Installation
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirement.txt.txt
Usage

Run notebooks in this order:

data_cleaning.ipynb
eda_chart.ipynb
preprocessing.ipynb
model-training.ipynb
evaluation.ipynb
Future Improvements
Deploy with Streamlit
Add real-time prediction API
Perform hyperparameter tuning
Experiment with advanced models (e.g., XGBoost)

License

For educational purposes.