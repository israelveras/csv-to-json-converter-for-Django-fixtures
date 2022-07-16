import csv
import json

csv_path = '/path-my-csv/file.csv'
json_output_file = '/path-out/namefile.json'
model_name = 'app.ModelName'

def read_csv_write_json(csv_file, json_file, app_model):
    csv_row = []
    with open(csv_file) as csv_f:
        csv_r = csv.DictReader(csv_f)
        field = csv_r.fieldnames
        id = 0
        for row in csv_r:
            id = id + 1
            csv_row.extend(
                [{"model": app_model, "pk": id, "fields": {field[i]: row[field[i]] for i in range(len(field))}}])
        converter_json(csv_row, json_output_file)

def converter_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
        f.write(json.dumps(data))

read_csv_write_json(csv_path, json_output_file, model_name)