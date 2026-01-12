from pathlib import Path
import logging
import requests

def fetch_registry(url: str, out_path: Path) -> Path:
    """
    Fetch the Navarra economic establishments registry CSV
    and save it to the raw data directory.

    Returns the path to the saved file.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)

    logging.info("Downloading %s", url)
    logging.info("Downloading…")
    r = requests.get(url, timeout=60)

    out_path.write_bytes(r.content)
    logging.info(
        "Saved raw file to %s (%d bytes)",
        out_path,
        out_path.stat().st_size,
    )

    return out_path
