# fileparse.py
#
# Exercise 3.4

import csv

def parse_csv(filename: str,select = None) -> list:
    records = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            records.append(record)
    new_records = []
    if select:
        for record in records:
            new_record = {key: record[key] for key in record.keys() if key in select}
            new_records.append(new_record)
        return new_records
    return records