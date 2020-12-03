# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename: str) -> list:
    records = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            record = dict(zip(header, row))
            records.append(record)
    return records