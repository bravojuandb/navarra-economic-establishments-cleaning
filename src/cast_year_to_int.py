import logging

import pandas as pd


def cast_year_to_int(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert and coerce string column 'anio' to nullable Int64.
    Log the count of non-null values casted to Int64.
    Log the year range.
    """

    df = df.copy()

    # Required column: abort pipeline if 'anio' is missing
    if "anio" not in df.columns:
        raise KeyError("Column 'anio' not found in DataFrame")

    df["anio"] = pd.to_numeric(df["anio"], errors="coerce").astype("Int64")

    non_null = int(df["anio"].notna().sum())
    year_min = int(df["anio"].min()) if non_null > 0 else None
    year_max = int(df["anio"].max()) if non_null > 0 else None

    logging.info(
        "Casted 'anio' to Int64; non-null=%d; range=%s–%s",
        non_null,
        year_min,
        year_max,
    )

    return df