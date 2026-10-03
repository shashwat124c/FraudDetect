"""FraudLens Interactive Fraud Detection Dashboard."""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="FraudLens | Financial Fraud Detection",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ FraudLens — Fraud Detection Platform")
st.markdown("Monitor transactions, investigate flagged anomalies, and evaluate fraud detection models.")

# Sidebar controls
st.sidebar.header("Navigation & Settings")
page = st.sidebar.radio("View", ["Live Scoring", "Model Performance", "Data Overview"])

if page == "Live Scoring":
    st.subheader("Transaction Risk Scoring")
    col1, col2 = st.columns(2)
    with col1:
        txn_type = st.selectbox("Transaction Type", ["TRANSFER", "CASH_OUT", "PAYMENT", "DEBIT", "CASH_IN"])
        amount = st.number_input("Amount ($)", min_value=0.0, value=15000.0, step=100.0)
    with col2:
        old_balance_orig = st.number_input("Sender Old Balance ($)", min_value=0.0, value=20000.0, step=100.0)
        new_balance_orig = st.number_input("Sender New Balance ($)", min_value=0.0, value=5000.0, step=100.0)

    if st.button("Evaluate Transaction"):
        # Placeholder heuristic rule / model scoring
        is_high_risk = txn_type in ["TRANSFER", "CASH_OUT"] and amount > 10000
        if is_high_risk:
            st.error("⚠️ High Fraud Risk Detected! Transaction flagged for review.")
        else:
            st.success("✅ Transaction is classified as Normal / Low Risk.")

elif page == "Model Performance":
    st.subheader("Model Evaluation & Cost Analysis")
    st.info("Train a model using notebooks or pipeline to display ROC-AUC, PR-AUC, and financial savings metrics here.")

elif page == "Data Overview":
    st.subheader("Raw Data & Feature Distribution")
    st.markdown("Data is located at `data/raw/Fraud.csv`.")
