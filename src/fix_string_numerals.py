import logging

import pandas as pd

def fix_string_numerals(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove the suffix .0 from selected string-numeral columns
    and log how many values were fixed.
    """

    df = df.copy()

    string_numeral_cols = ["cnae09_ppal", "cnae09_local", "portalt"]
    total_fixed_values = 0

    # Required columns: abort pipeline if any string numeral column is missing
    missing_cols = [col for col in string_numeral_cols if col not in df.columns]
    if missing_cols:
        raise KeyError(f"Missing required columns for fix_string_numerals: {', '.join(missing_cols)}")

    for col in string_numeral_cols:
        fixed = df[col].str.endswith(".0", na=False).sum()
        df[col] = df[col].str.replace(r"\.0$", "", regex=True)
        total_fixed_values += int(fixed)

    logging.info("Fixed %d string-numeral values", total_fixed_values)

    return df
