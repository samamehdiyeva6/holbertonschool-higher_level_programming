import csv
import json

def convert_csv_to_json(filename):
    with open(filename, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
    try:
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(reader, f)
            return True
    except FileNotFoundError:
        return False
