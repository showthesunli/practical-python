from follow import follow
from typing import List, Dict
from report import read_portfolio
from portfolio import Portfolio
from tableformat import createFormatter
import csv

def filter_symbols(rows: List[Dict], portfolio: Portfolio):
    for row in rows:
        if row['name'] in portfolio:
            yield row

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

def tricker(portfolio_file:str, sotck_log_file: str, fmt:str):
    #parse stock data
    it_follow = follow(sotck_log_file)
    rows = parse_stock_data(it_follow)
    #filter stock data
    portfolio = read_portfolio(portfolio_file)
    rows = filter_symbols(rows, portfolio)
    #format and output
    formater = createFormatter(fmt)
    formater.heading(('name', 'price', 'change'))
    for row in rows:
        formater.row((row['name'], f'{row["price"]}', f'{row["change"]}'))


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 4:
        raise SystemExit(f'Usage: python {sys.argv[0]} portfoliofile stocklogfile fmt')
    tricker(sys.argv[1], sys.argv[2], sys.argv[3])
    