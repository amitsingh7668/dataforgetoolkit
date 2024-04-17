
# Project Title

DataForgeToolkit is a Python library for mapping CSV or Excel files based on JSON transformation mappings.


## Installation

Install my-project with npm

```bash
  pip install dataforgetoolkit
```
    
## Usage/Examples

```python
    from dataforgetoolkit import datamapper

    mapped_data = datamapper.map(report_file_path, transformation_file_path)

```


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

