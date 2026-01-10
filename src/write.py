"""
This is the last processing step, 
it will write to csv for now for debuging purposses
"""

from pathlib import Path
import pandas as pd


def write(df: pd.DataFrame, output_path: Path) -> Path:
    if df.empty:
        raise ValueError("DataFrame is empty")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_csv(output_path, index=False)
    return output_path