#! /usr/bin/env python
# report.py
#
# Exercise 3.18
import csv
import pprint
from fileparse import parse_csv

def read_portfolio(filename: str) -> list:
    """
    read stock prices to dict from portfolio.csv
    """
    with open(filename, 'rt') as f:
        portfolio = fileparse.read_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
            
    return portfolio

def read_prices(filename: str) -> dict: 
    """
    read stock prices to dict from prices.csv
    """
    with open(filename, 'rt') as f:
        prices = fileparse.read_csv(f, types=[str, float], hashead=False)
    prices = dict(prices)
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
    with open(portfolio, 'rt') as f:
        portfolio = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    
    with open(prices, 'rt') as f:
        prices = dict(parse_csv(f, types=[str, float], hashead=False))

    print_report(portfolio, prices)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: python {sys.argv[0]} portfoliofile pricesfile')

    portfolio = sys.argv[1]
    prices = sys.argv[2]
    portfolio_report(portfolio, prices)
        