# fileparse.py
#
# Exercise 3.5

import csv

def parse_csv(filename: str, select: list = None, types: list = None, hashead = True) -> list:
    records = [] 
    indes = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows) if hashead else []

        if select:
            indes = [header.index(key) for key in select]
            header = select
        for row in rows:
            record = row

            if indes:
                record = [row[i] for i in indes]
            if types:
                record = [func(val) for func, val in zip(types, row)]
            
            if hashead:
                records.append(dict(zip(header, record)))
            else:

                records.append(tuple(record))
    return records
     