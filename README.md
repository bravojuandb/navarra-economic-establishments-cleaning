# navarra-data-batch-pipeline

A reproducible batch data pipeline that standardizes Navarra’s official economic establishments registry.

**Input:** raw CSV (kept immutable)  
**Output:** validated Parquet (`data/processed/navarra_processed.parquet`)  
**Goal:** produce an analysis-ready dataset through deterministic cleaning, type enforcement, deduplication, and validation.

## Contents

- [Purpose](#purpose)
- [Data Cleaning Contract](#data-cleaning-contract)
- [Pipeline overview](#pipeline-overview)
- [How to run](#how-to-run)

## Purpose

This project processes a public registry of economic establishments in Navarra covering the years 2018–2025, with the goal of producing a consistent, analysis-ready dataset.

**Non-goals:** database loading, analytics, dashboards, enrichment or entity resolution.

## Raw dataset

The raw dataset is provided as a CSV from public sources.
Each row represents a registered economic establishment or self-employed activity for a given year in Navarra. 
More info about the dataset [here](data/raw/README.md).

## Data cleaning contract

This dataset contains administrative records from multiple years,
and many fields are inconsistently formatted or partially missing.

The pipeline applies the following rules:

1. **Standardize missing and invalid values into explicit nulls** (empty strings, placeholders like . or 0) 
2. **Enforce data types** (years -> integers, codes and identifiers -> strings)
3. **Preserve identifier columns as strings** (e.g. dnici, codpost, cod_cmun, codigo_entidad)
4. **Clean obvious formatting issues** (trim leading/trailing spaces , remove .0 from CNAE codes and adress numbers)
5. **Keep free-text fields** (addresses, names, descriptions) untouched except for basic trimming
6. **Remove only exact duplicate rows**

After this process (guarantees):

- Raw input file is never modified 
- All columns are read as strings to prevent automatic coercion.
- Missing or invalid values are explicitly standardized to pd.NA.
- Only one column (anio) is intentionally cast to a nullable integer type (Int64).
- Codes and identifiers are preserved as strings to retain their identifier semantics.
- Formatting artifacts (such as trailing .0 from numeric parsing) are removed only in code-like fields.
- Free-text fields are left untouched except for basic trimming.
- No structural changes or normalization are applied.

The result is a clean dataset in parquet format that can be safely reused for further processing or modeling.

## Pipeline overview

Raw CSV
→ fetch_data (if True)
→ read 
→ trim_whitespace
→ handle_nulls
→ fix_string_numerals
→ cast_year_to_int
→ dedupe_rows
→ validate (schema + invariants)
→ write_to_parquet

## Example tranformation

```md
| Column     | Raw value        | Cleaned value        |
|------------|------------------|----------------------|
| anio       | "2021.0"         | 2021 (Int64)         |
| dnici      | "G31189269"      | "G31189269" (string) |
| nombre     | "     "          | null                 |
| portalt    | "5.0"            | "5" (string)         |
| restot     | ".", "- -"       | null                 |
| cnae09 cods| "6910.0"         | "6910" (string)      |
```

## How to run

This project follows a simple fetch → clean workflow.

1. Clone the repository:
```bash
git clone https://github.com/bravojuandb/navarra-economic-establishments-cleaning.git
```
2. Install requirements.txt

3. Run the pipeline:

```bash
python -m src.run_pipeline
```
