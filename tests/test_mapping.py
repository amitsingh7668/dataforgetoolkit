import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory (assuming the source module is located in the src directory)
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the sys.path
sys.path.insert(0, parent_dir)

from datawizard.datamapper import map_data


def test_map_data():
    report_file_path = "datawizard/datawizard/utils/data.csv"
    transformation_file_path = "datawizard/datawizard/utils/mapping.json"
    result = map_data(report_file_path, transformation_file_path)
    print(result)
    assert result == [{'Student Name': 'Amit Singh', 'Age': 30}, {
        'Student Name': 'Amit Singh', 'Age': 25}, {'Student Name': 'Amit Singh', 'Age': 35}]

