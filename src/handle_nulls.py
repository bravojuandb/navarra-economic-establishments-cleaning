import logging

import pandas as pd


def handle_nulls(df: pd.DataFrame, verbose: bool = False) -> pd.DataFrame:
    """
    Deterministic null conversion. Non destructive process.
    - Replace empty strings with pd.NA
    - Replace placeholder tokens with pd.NA.
    - Do not edit valid values.
    """
    df = df.copy()

    if verbose:
        before = df.isna().sum().sum()

    df[df.columns] = df[df.columns].replace("", pd.NA)

    placeholders: dict[str, dict[str, object]] = {
        # Invalid tokens by column, interpreted as pd.NA
        "portalt": {
            "0": pd.NA,
            "0.0": pd.NA,
        },
        "restot": {
            ".": pd.NA,
            ". .": pd.NA,
            "--": pd.NA,
            "-": pd.NA,
            "- -": pd.NA,
            "99": pd.NA,
        },
        "codpost": {
            "0": pd.NA
        }
    }

    for col, mapping in placeholders.items():
        if col in df.columns:
            df[col] = df[col].replace(mapping)

    if verbose:
        after = df.isna().sum().sum()
        logging.info("Converted %d values to pd.NA", (after - before))

    return df
