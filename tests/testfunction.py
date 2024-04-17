from dataforgetoolkit import datamapper

def test_map_data():
    datamapper.map_data("dataforgetoolkit/tests/utils/data.csv", "dataforgetoolkit/tests/utils/mapping.json")

print(test_map_data())