from follow import follow
from typing import List
import csv

def make_dict(rows: List, header: List[str]):
    for row in rows:
        yield dict(zip(header, row))

def convert_type(rows: List, types: List):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def select_colum(rows: List, indes: List[int]):
    for row in rows:
        yield [row[index] for index in indes]

def parse_stock_data(csvflie):
    reader = csv.reader(csvflie)
    rows = select_colum(reader, [0, 1, 4])
    rows = convert_type(rows, [str, float, float])
    rows = make_dict(rows, ['name', 'price', 'change'])
    return rows

if __name__ == '__main__':
    it_follow = follow('Data/stocklog.csv')
    rows = parse_stock_data(it_follow)
    for row in rows:
        print(row)