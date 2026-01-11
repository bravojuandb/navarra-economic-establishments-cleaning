from pathlib import Path
import logging

import pandas as pd


def read(path: Path) -> pd.DataFrame:
    """Read raw registry CSV from disk.

    - Read all columns as strings.
    - Disable Pandas automatic NA parsing.
    - Fail fast if the file is missing or the CSV.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"Raw data file not found: {path}")

    return pd.read_csv(
        path,
        dtype="string",
        keep_default_na=False,
    )

