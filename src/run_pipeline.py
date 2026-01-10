from pathlib import Path
import logging

from src.read import read
from src.trim_whitespace import trim_whitespace
from src.handle_nulls import handle_nulls

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

base_dir = Path(__file__).resolve().parent.parent
file_path = base_dir / "data" / "raw" / "economic_establishments_navarra.csv"

#------- READ
logging.info("Reading file: %s", file_path.name)
df = read(file_path)
logging.info("Loaded %d rows", len(df))

#------- TRIM WHITESPACES
df = trim_whitespace(df, verbose=True)


#------- HANDLE NULL VALUES 
df = handle_nulls(df, verbose=True)






logging.info("Pipeline completed successfully")