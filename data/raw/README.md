## Raw data description

The raw dataset is provided as a CSV file.  

Each row represents a registered economic establishment or self-employed activity for a given year in Navarra.



The dataset contains the following columns:

- **_id**  
  Internal row unique identifier.

- **anio**  
  Year the record refers to. The year span is 2018-2025

- **dnici**  
  Spanish ID of the person or entity associated with the economic activity.  

- **nombre**  
  Registered name of the person or entity, usually formatted as comma-separated surnames and given names.  

- **msiglat**  
  Street type of the address (e.g. Calle, Avenida, Plaza).

- **callet**  
  Street name of the registered address.

- **portalt**  
  Building or portal number of the address.  

- **restot**  
  Additional address information such as floor, door, unit, or other qualifiers.

- **codpost**  
  Postal code of the registered address.  

- **cod_cmun**  
  Municipality code identifying the municipality where the establishment is registered.

- **nombre_cmun**  
  Municipality name, often presented in bilingual format (Spanish / Basque).

- **codigo_entidad**  
  Legal entity identifier, when applicable.  
  This field is frequently empty.

- **denominacion_entidad**  
  Legal entity name, when applicable.  
  This field is frequently empty.

- **tramo_asal**  
  Employment size range associated with the activity.

- **cnae09_ppal**  
  Main economic activity code according to the CNAE 2009 classification.  

- **cnae09_descrip_ppal**  
  Textual description of the main CNAE activity.  

- **cnae09_local**  
  CNAE 2009 code corresponding to the local activity at the registered address.  
  May differ from the main CNAE code.

- **cnae09_descrip_local**  
  Textual description of the local CNAE activity.  
  Often missing in the source data.

### Notes on raw data quality

- The raw dataset contains missing values, inconsistent formatting, and mixed data types.
- Identifiers and classification codes are sometimes stored as numeric values despite representing categorical codes.
- Municipality names and address components are not standardized.
- The raw data is preserved unchanged and treated as the source of truth for all transformations.