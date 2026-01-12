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


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

def main() -> None:
    base_dir = Path(__file__).resolve().parent.parent
    raw_input_path = base_dir / "data" / "raw" / "economic_establishments_navarra.csv"
    processed_output_path = base_dir / "data" / "processed" / "navarra_processed.parquet"

    #-------  DOWNLOAD DATA
    DOWNLOAD_INPUT_DATA = False
    if DOWNLOAD_INPUT_DATA:
        from src.fetch_data import fetch_registry
        url = "https://datosabiertos.navarra.es/datastore/dump/0c4b4747-026f-479a-9966-6568a88957f5?format=csv&bom=True"
        fetch_registry(url=url, out_path= raw_input_path)

    #-------  READ
    logging.info("Reading file: %s", raw_input_path.name)
    df = read(raw_input_path)
    logging.info("Loaded %d rows", len(df))

    #-------  TRANSFORMS
    df = trim_whitespace(df, verbose=True)
    df = handle_nulls(df, verbose=True)
    df = fix_string_numerals(df)
    df = cast_year_to_int(df)
    df = dedupe_rows(df)

    #-------  VALIDATE PIPELINE
    df = validate(df)

    #-------  DEBUG CSV (OPTIONAL) 
    DEBUG_WRITE_CSV = True
    if DEBUG_WRITE_CSV:
        from src.write import write
        write(df, base_dir / "data" / "processed" / "output_sample.csv")

    #-------  FINAL OUTPUT 
    write_to_parquet(df, output_path=processed_output_path)
    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()