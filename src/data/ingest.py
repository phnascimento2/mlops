import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv")

def load_data(path: Path = RAW_DATA_PATH) -> pd.DataFrame:
    """Load raw churn dataset"""
    return pd.read_csv(path)

def validate_data(df: pd.DataFrame) -> None:
    """Quick validation checks"""
    assert "customerID" in df.columns, "Missing customerID column"
    assert df.shape[0] > 0, "Empty dataset."

if __name__ == "__main__":
    df = load_data()
    validate_data(df)
    print(df.head())
