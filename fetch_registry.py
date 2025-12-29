# This script downloads the CSV report from the official source
# and saves it to data/raw (raw layer).

#!/usr/bin/env python3
from pathlib import Path
import logging
import requests

URL = "https://datosabiertos.navarra.es/datastore/dump/0c4b4747-026f-479a-9966-6568a88957f5?format=csv&bom=True"

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = PROJECT_ROOT / "data/raw/economic_establishments_navarra.csv"

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(message)s")
log = logging.getLogger("fetch")


def fetch_registry(url: str = URL, out_path: Path = OUT_PATH) -> Path:
    """
    Fetch the Navarra economic establishments registry CSV
    and save it to the raw data directory.

    Returns the path to the saved file.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    log.info("Downloading %s", url)
    log.info("Downloading…")
    r = requests.get(url, timeout=60)

    out_path.write_bytes(r.content)
    log.info(
        "Saved raw file to %s (%d bytes)",
        out_path,
        out_path.stat().st_size,
    )

    return out_path


def main() -> None:
    fetch_registry()


if __name__ == "__main__":
    main()