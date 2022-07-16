import csv
import json

csv_path = '/path-my-csv/file.csv'
json_output_file = '/path-out/namefile.json'
model_name = 'app.ModelName'

def read_csv_write_json_setting_id(csv_file, json_file, app_model):
    csv_row = []
    with open(csv_file) as csv_f:
        csv_r = csv.DictReader(csv_f)
        field = csv_r.fieldnames
        for row in csv_r:
            csv_row.extend([{"model": app_model, "pk": row[field[0]], "fields": {field[i]:row[field[i]] for i in range(1, len(field))}}])
        convert_write_json(csv_row, json_output_file)

def convert_write_json(data, json_file):
    with open(json_file, "w") as f:
        f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
        f.write(json.dumps(data))

read_csv_write_json_setting_id(csv_path, json_output_file, model_name)