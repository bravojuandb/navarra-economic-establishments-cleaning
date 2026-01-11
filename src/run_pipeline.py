from pathlib import Path
import logging

from src.read import read
from src.trim_whitespace import trim_whitespace
from src.handle_nulls import handle_nulls
from src.fix_string_numerals import fix_string_numerals
from src.cast_year_to_int import cast_year_to_int
from src.dedupe_rows import dedupe_rows
from src.validate import validate
from src.write_to_parquet import write_to_parquet

from src.write import write

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

base_dir = Path(__file__).resolve().parent.parent
input_path = base_dir / "data" / "raw" / "economic_establishments_navarra.csv"
output_path = base_dir / "data" / "processed" / "navarra_processed.parquet"


#------- READ
logging.info("Reading file: %s", input_path.name)
df = read(input_path)
logging.info("Loaded %d rows", len(df))

#------- TRIM WHITESPACES
df = trim_whitespace(df, verbose=True)

#------- HANDLE NULL VALUES 
df = handle_nulls(df, verbose=True)

#------- FIX STRING NUMERALS
df = fix_string_numerals(df)

#------- ENFORCE DATA TYPE INT64

df = cast_year_to_int(df)

#------- REMOVE DUPLICATE ROWS

df = dedupe_rows(df)

#------- VALIDATE PIPELINE

df = validate(df)

#-------  WRITE TO CSV (FOR DEBUGGING PURPOSE ONLY) 

DEBUG_WRITE_CSV = False

if DEBUG_WRITE_CSV:
    write(df, base_dir / "data" / "processed" / "output_sample.csv")

#-------  WRITE TO PARQUET (FINAL STEP) 

write_to_parquet(df, output_path=output_path)

logging.info("Pipeline completed successfully")