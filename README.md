# FraudLens 🛡️

FraudLens is an end-to-end financial transaction fraud detection system equipped with exploratory analysis, feature engineering, cost-sensitive machine learning, and interactive alerting dashboards.

## Project Structure

```text
fraudlens/
├── data/
│   ├── raw/                 # Original transaction records (e.g., Fraud.csv)
│   └── processed/           # Cleaned & feature-engineered datasets
├── notebooks/
│   ├── 01_data_understanding.ipynb   # Initial EDA & data distributions
│   ├── 02_fraud_analysis.ipynb       # Deep dive into fraud patterns & behavioral indicators
│   └── 03_modeling.ipynb             # ML model training, PR-AUC tuning, cost metrics
├── src/
│   ├── preprocessing.py     # Data ingestion, schema validation, cleaning
│   ├── features.py          # Balance delta and behavioral feature pipelines
│   └── cost_analysis.py     # Financial cost-benefit and threshold evaluation
├── models/                  # Serialized trained model artifacts (.joblib / .pkl)
├── app.py                   # Streamlit interactive detection & monitoring dashboard
├── requirements.txt         # Project dependencies
└── README.md
```

## Quick Start

### 1. Environment Setup

```bash
python -m venv venv
# Windows:
.\venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Run the Notebooks

Launch JupyterLab to walk through the analysis stages:

```bash
jupyter lab
```

1. [01_data_understanding.ipynb](file:///c:/Projects/FraudDetector/notebooks/01_data_understanding.ipynb)
2. [02_fraud_analysis.ipynb](file:///c:/Projects/FraudDetector/notebooks/02_fraud_analysis.ipynb)
3. [03_modeling.ipynb](file:///c:/Projects/FraudDetector/notebooks/03_modeling.ipynb)

### 3. Launch Web App

```bash
streamlit run app.py
```
