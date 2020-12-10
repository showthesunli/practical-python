#! /usr/bin/env python
# report.py
#
# Exercise 4.4
import csv
import pprint
from fileparse import parse_csv
from stock import Stock

def read_portfolio(filename: str) -> list:
    """
    read stock prices to dict from portfolio.csv
    """
    with open(filename, 'rt') as f:
        file_content = parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [Stock(row['name'], row['shares'], row['price']) for row in file_content]
    return portfolio

def read_prices(filename: str) -> dict: 
    """
    read stock prices to dict from prices.csv
    """
    with open(filename, 'rt') as f:
        prices = parse_csv(f, types=[str, float], hashead=False)
    prices = dict(prices)
    return prices

def make_report_data(portfolio: list, prices: dict) ->list:
    '''
    make raw data of report
    '''
    report = []
    report.append(('name', 'Shares', 'Price', 'Change'))
    for stock in portfolio:
        change = prices[stock.name] - stock.price
        report.append((stock.name, stock.shares, stock.price, change))
    intres = 0.00
    total_cost = 0.00
    for i in portfolio:
        cost_of_one_share = stock.shares*stock.price
        intres_of_one_share = prices[stock.name]*stock.shares - cost_of_one_share
        total_cost += cost_of_one_share
        intres += intres_of_one_share
    count = {'intres':intres,'total_cost':total_cost}
    report.append(count)
    return report

def print_report(rawdata: list) -> list:
    '''
    print the report of portfolio
    '''
    header = rawdata[0]
    print(f'{header[0]:>10s} {header[1]:>10s} {header[2]:>10s} {header[3]:>10s}')
    print(('-'*10+' ')*4)
    for row in rawdata[1:-1]:
        print(f'{row[0]:>10s} {row[1]:10d} {row[2]:10.2f} {row[3]:10.2f}')
    count = rawdata[-1]
    print(f'intres: {count["intres"]:.2f} total_cost: {count["total_cost"]:.2f}')

def portfolio_report(portfolio: str, prices: str):
    '''
    read portfolio and prices files, then print the report
    '''
   
    portfolio = read_portfolio(portfolio)


    prices = read_prices(prices)
    rawdata = make_report_data(portfolio, prices)
    print(rawdata[-1])

    print_report(rawdata)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        raise SystemExit(f'Usage: python {sys.argv[0]} portfoliofile pricesfile')

    portfolio = sys.argv[1]
    prices = sys.argv[2]
    portfolio_report(portfolio, prices)
        