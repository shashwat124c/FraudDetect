"""Feature engineering module for FraudLens."""

import numpy as np
import pandas as pd


def generate_balance_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create balance discrepancy and ratio features.

    Features created:
    - error_balance_orig: Difference between newbalanceOrig and (oldbalanceOrg - amount)
    - error_balance_dest: Difference between (oldbalanceDest + amount) and newbalanceDest
    - amount_to_orig_ratio: Transaction amount relative to original balance
    """
    df = df.copy()

    if {"oldbalanceOrg", "newbalanceOrig", "amount"}.issubset(df.columns):
        df["error_balance_orig"] = df["newbalanceOrig"] + df["amount"] - df["oldbalanceOrg"]
        df["amount_to_orig_ratio"] = df["amount"] / (df["oldbalanceOrg"] + 1.0)

    if {"oldbalanceDest", "newbalanceDest", "amount"}.issubset(df.columns):
        df["error_balance_dest"] = df["oldbalanceDest"] + df["amount"] - df["newbalanceDest"]

    return df


def encode_transaction_types(df: pd.DataFrame, type_col: str = "type") -> pd.DataFrame:
    """One-hot encode categorical transaction types."""
    if type_col in df.columns:
        return pd.get_dummies(df, columns=[type_col], drop_first=False)
    return df
