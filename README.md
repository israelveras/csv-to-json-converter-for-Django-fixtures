# csv-to-json-converter-for-Django-fixtures

Two simple and practical algorithms that convert csv file into json in the format read by Django when loading fixtures.

Algorithm **csv_to_json_Django_fixtures.py** generates the id incrementally without you having to reserve a column for id in the csv file.

In **csv_to_json_setting_id.py** you need to reserve the first column of csv with the ids you want to set.