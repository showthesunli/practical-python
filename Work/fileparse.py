# fileparse.py
#
# Exercise 3.10

import csv

def parse_csv(filename: str, select: list = None, types: list = None, hashead = True, delimiter = ',', silece_error = True):
    if select and not hashead:
        raise RuntimeError('select argument requires colum header')

    records = [] 
    indes = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f, delimiter = delimiter)

        header = next(rows) if hashead else []

        if select:
            indes = [header.index(key) for key in select]
            header = select

        for rowno, row in enumerate(rows):
            if not row:
                continue

            record = row
            try:
                if indes:
                    record = [row[i] for i in indes]
                if types:
                    record = [func(val) for func, val in zip(types, row)]
                if hashead:
                    records.append(dict(zip(header, record)))
                else:
                    records.append(tuple(record))   
            except ValueError as e:
                if not silece_error:
                    print('rowno: ', rowno, 'reason', e)
                    print('rowno: ', rowno, 'can\'t convert', row)
    return records
     