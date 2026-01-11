import pandas as pd

import logging


def dedupe_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove exact duplicate rows using default pandas behavior.
    """

    df = df.copy()

    before = len(df)
    df = df.drop_duplicates()
    after = len(df)

    logging.info(f"Deduplicated rows: %d", before - after)

    return df
