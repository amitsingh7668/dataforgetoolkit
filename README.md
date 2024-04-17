
# Project Title

DataForgeToolkit is a Python library for mapping CSV or Excel files based on JSON transformation mappings.

# Description

DataForgeToolkit: Flexible Data Mapping for CSV/XLSX Files

The DataForgeToolkit is a Python library designed to streamline the process of converting CSV or Excel files into customized DataFrames based on user-defined JSON mapping configurations. Whether you're working with financial reports, customer datasets, or any other structured data, this toolkit empowers you to effortlessly transform raw data into actionable insights.

Features:
Versatile File Support: Seamlessly process both CSV and Excel files, providing flexibility in handling various data formats commonly encountered in data analysis tasks.

Customizable Mapping: Define transformation mappings using a JSON file, allowing for precise specification of column names, data cleaning, and value substitutions tailored to your specific data requirements.

Efficient Data Processing: Automate data preprocessing tasks such as handling missing values, standardizing column names, and applying complex value mappings with ease.


## Installation Usage/Examples


```bash
  pip install dataforgetoolkit
```
    
Define Transformation Mapping:

Create a JSON file specifying the transformation mappings for your data. Define column mappings, specify new column names, and define value substitutions as needed.

Use the Toolkit:

Import the DataForgeToolkit in your Python script and utilize the map function to convert your report files:

```bash
    from dataforgetoolkit import datamapper
    datamapper.map('report file path csv / xlsx format','mapping json file path')
```

Access Mapped Data:

Access the transformed data as a DataFrame for further analysis or export to other formats.


## JSON Transformation Mapping

 Transformation mappings are specified using a JSON file. Example:

    {
        "transformation_mapping": [
            {
                "column": "Name",
                "new_name": "Student Name",
                "value_mappings": [
                    {
                        "*": "Amit Singh"
                    }
                ]
            },
            {
                "column": "Age_Column",
                "new_name": "Age",
                "value_mappings": [
                    {
                        "FILTER": "30"
                    }
                ]
            }
        ]
    }


## Authors

- [@amitsingh](https://github.com/amitsingh7668/)

- Software Engineer
## Contributing

Contributions are always welcome!

Please adhere to this project's `code of conduct`.

Suggest code and open PR/MR


## Used By

'Intended Audience' :: Developers , Testers , BA

