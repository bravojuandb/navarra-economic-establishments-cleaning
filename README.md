# navarra-economic-establishments-cleaning

Cleaning the official Directory of Economic Establishments in Navarra (Spain) for analytical and statistical use.

## Contents

- [Purpose](#purpose)
- [Raw Dataset](#raw_dataset)
- [Data Cleaning Contract](#data_cleaning_contract)

## Purpose

This project cleans a public registry of economic establishments in Navarra covering the years 2018–2025, with the goal of producing a consistent, analysis-ready dataset.

## Raw dataset

The raw dataset is provided as a CSV file, fetched from public sources.
Each row represents a registered economic establishment or self-employed activity for a given year in Navarra. 
More info about the dataset [here](data/raw/README.md).

## Data cleaning contract

This dataset contains administrative records from multiple years,
and many fields are inconsistently formatted or partially missing.

The cleaning process follows these simple rules:

1. **Standardize missing values into explicit nulls** (empty strings, placeholders like . or 0) 
2. **Enforce data types** (years -> integers, codes and identifiers -> strings)
3. **Preserve leading zeros and alphanumeric identifiers** (e.g. dnici, postal and municipality codes)
4. **Clean obvious formatting issues** (trim spaces, remove .0 from CNAE codes)
5. **Keep free-text fields** (addresses, names, descriptions) untouched except for basic trimming
6. **Remove only exact duplicate rows**

After this process, the dataset has:

- the same columns as the raw data
- consistent types and null handling across all years
- no structural changes or normalization

The result is a clean dataset that can be safely reused for further processing or modeling.





