import pandas as pd
import logging

def validate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate core pipeline invariants
    """

    if df.empty:
        raise ValueError("Validation failed: DataFrame is empty")

    if str(df['anio'].dtype) != "Int64":
        raise TypeError(
            f"Validation failed: 'anio' must have dtype Int64, got {df['anio'].dtype}"
        )
    
    # No empty or whitespace-only strings allowed in string-like columns
    # It assumes string colums are in fact string type
    str_cols = df.select_dtypes(include=["string"]).columns
    for col in str_cols:
        s = df[col]
        if ((s.notna()) & (s.str.strip() == "")).any():
            raise ValueError(f"Validation failed: empty strings found in column '{col}'")

    logging.info("Validation passed")
    return df