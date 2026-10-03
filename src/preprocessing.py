"""Data preprocessing utilities for FraudLens."""

from pathlib import Path
from typing import Optional, Tuple
import pandas as pd


def load_raw_data(data_path: str = "data/raw/Fraud.csv", nrows: Optional[int] = None) -> pd.DataFrame:
    """Load the raw fraud dataset.

    Args:
        data_path: Path to the raw CSV file.
        nrows: Optional limit on number of rows to load.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    path = Path(data_path)
    if not path.exists():
        raise FileNotFoundError(f"Raw data file not found at {data_path}")
    return pd.read_csv(path, nrows=nrows)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform baseline cleaning on fraud transactions data.

    Args:
        df: Input DataFrame.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    cleaned = df.copy()
    # Ensure column names are standardized
    cleaned.columns = [col.strip() for col in cleaned.columns]
    return cleaned


def save_processed_data(df: pd.DataFrame, output_path: str = "data/processed/cleaned_fraud.parquet") -> None:
    """Save processed dataset to disk in Parquet or CSV format."""
    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix == ".parquet":
        df.to_parquet(out, index=False)
    else:
        df.to_csv(out, index=False)
