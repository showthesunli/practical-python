#! /usr/bin/env python
# report.py
#
# Exercise 3.15
import csv
import pprint
from fileparse import parse_csv

def read_portfolio(filename: str) -> list:
    """
    read stock prices to dict from portfolio.csv
    """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            try:
                record = dict(zip(header, row))
                portfolio.append({
                    'name': record['name'],
                    'shares': int(record['shares']),
                    'price': float(record['price'])
                })
            except ValueError as identifier:
                pass
            
    return portfolio

def read_prices(filename: str) -> dict: 
    """
    read stock prices to dict from prices.csv
    """
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except Exception as identifier:
                pass
    return prices

def print_report(portfolio: list, prices: dict) -> list:
    '''
    calculate and print the report of portfolio
    '''
    report = []
    report.append(('name', 'Shares', 'Price', 'Change'))
    for i in portfolio:
        change = prices[i['name']] - i['price']
        report.append((i['name'], i['shares'], i['price'], change))
    intres = 0.00
    total_cost = 0.00
    for i in portfolio:
        cost_of_one_share = i['shares']*i['price']
        intres_of_one_share = prices[i['name']]*i['shares'] - cost_of_one_share
        total_cost += cost_of_one_share
        intres += intres_of_one_share
    # report.append({'intres': intres, 'totcal_cost': total_cost})
    
    #print report
    
    header = report[0]
    print(f'{header[0]:10s} {header[1]:10s} {header[2]:10s} {header[3]:10s}')
    print(('-'*10+' ')*4)
    for row in report[1:]:
        print(f'{row[0]:10s} {row[1]:10d} {row[2]:10.2f} {row[3]:10.2f}')
    print(f'intres: {intres:10.2f} total_cost: {total_cost:10.2f}')

def portfolio_report(portfolio: str, prices: str):
    '''
    read portfolio and prices files, then print the report
    '''
    portfolio = parse_csv(portfolio, select=['name', 'shares', 'price'], types=[str, int, float])
    prices = dict(parse_csv(prices, types=[str, float], hashead=False))

    print_report(portfolio, prices)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: python {sys.argv[0]} portfoliofile pricesfile')

    portfolio = sys.argv[1]
    prices = sys.argv[2]
    portfolio_report(portfolio, prices)
        