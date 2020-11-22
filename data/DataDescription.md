# Dataset Description  

### Person Dataset (Column 0 - Column 5)  
Data for each person in the EHR system. A total of 49,982 features with access to demographic data. Columns which we could not find mappings for including provider have been removed.

### Gold Standard Dataset (Column 6)
The result of the test with 0: negative, and 1: positive.

### Observation Dataset (Column 7 - Column 9)
General observations based data: Alcohol, Oxygen Saturation and Tobacco Use.

### Visit Dataset (Column 10 - Column 16)
Patient visit or access of the healthcare system. This includes number of visits, calls, and telehealth.

### Measurement Dataset(Column 17 - 1984)
Contains other measured values, with 4 columns for each measurement type. 4 columns are: value, date, range_high, range_low. These set of columns would require the most cleaning as some are vary sparsely populated.



