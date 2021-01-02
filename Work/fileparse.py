# fileparse.py
#
# Exercise 3.10

import csv
from typing import Any

def parse_csv(lines, select: list = None, types: list = None, hashead = True, delimiter = ',', silece_error = True):
    

    if select and not hashead:
        raise RuntimeError('select argument requires colum header')

    records: Any = [] 
    indes = []
    
    rows = csv.reader(lines, delimiter = delimiter)

    header = next(rows) if hashead else []

    if select:
        indes = [header.index(key) for key in select]
        header = select

    for rowno, row in enumerate(rows):
        if not row:
            continue

        record: Any = row
        try:
            if indes:
                record = [row[i] for i in indes]
            if types:
                record = [func(val) for func, val in zip(types, record)]
            if hashead:
                records.append(dict(zip(header, record)))
            else:
                records.append(tuple(record))   
        except ValueError as e:
            if not silece_error:
                print('rowno: ', rowno, 'reason', e)
                print('rowno: ', rowno, 'can\'t convert', row)
    
    return records
     