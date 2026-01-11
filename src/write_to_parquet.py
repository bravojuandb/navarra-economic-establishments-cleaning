from pathlib import Path
import logging
import pandas as pd


def write_to_parquet(df: pd.DataFrame, output_path: Path) -> Path:
    """
    Write DataFrame to Parquet format.
    Assumes parent directories may not exist.
    """

    if df.empty:
        raise ValueError("Refusing to write empty DataFrame to Parquet")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        df.to_parquet(output_path, index=False)
    except ImportError as e:
        raise ImportError(
            "Parquet support requires 'pyarrow' or 'fastparquet'. "
            "Install one of them, e.g. `pip install pyarrow`."
        ) from e

    logging.info("File written to Parquet: %s", output_path.name)
    return output_path