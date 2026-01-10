from pathlib import Path
import logging

import pandas as pd

def trim_whitespace(df: pd.DataFrame, verbose: bool = False) -> pd.DataFrame:
    """
    Trim leading/trailing whitespace from all columns.
    This step assumes all columns are strings
    """

    if df.empty:
        raise ValueError(f"DataFrame is empty")

    df = df.copy()

    if verbose:
        before = df.apply(lambda s: s.str.len()).sum().sum()

    cols = df.columns
    df[cols] = df[cols].apply(lambda s: s.str.strip())

    if verbose:
        after = df.apply(lambda s: s.str.len()).sum().sum()
        logging.info("Trimmed %d whitespace characters", before - after)

    return df

if __name__ == "__main__":

    trim_whitespace()