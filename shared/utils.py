import pandas as pd
import matplotlib.pyplot as plt

CHURN_COLOR  = '#E8593C'
RETAIN_COLOR = '#3B8BD4'
NEUTRAL_COLOR = '#888780'

def load_data(path='../data/WA_Fn-UseC_-Telco-Customer-Churn.csv'):
    df = pd.read_csv(path)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce').fillna(0)
    df['Churn_Binary'] = df['Churn'].map({'Yes': 1, 'No': 0})
    df['SeniorCitizen_Label'] = df['SeniorCitizen'].map({1: 'Senior', 0: 'Non-Senior'})
    bins = [0, 12, 24, 48, 72]
    labels = ['0-12 mo', '13-24 mo', '25-48 mo', '49-72 mo']
    df['Tenure_Group'] = pd.cut(df['tenure'], bins=bins, labels=labels, include_lowest=True)
    return df

def set_style():
    plt.rcParams.update({
        'figure.dpi': 120,
        'axes.spines.top': False,
        'axes.spines.right': False,
        'axes.titlesize': 13,
        'axes.titleweight': 'bold',
    })