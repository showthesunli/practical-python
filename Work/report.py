#! /usr/bin/env python
# report.py
#
# Exercise 4.6
import csv
import pprint
from fileparse import parse_csv
from stock import Stock
from tableformat import TextTableFormatter, CSVTableFormatter, TableFormatter, createFormatter
from typing import TypeVar, List, Dict, Tuple, Any, Optional
from portfolio import Portfolio

def read_portfolio(filename: str, **opts) -> Portfolio:
    """
    read stock prices to dict from portfolio.csv
    """
    with open(filename, 'rt') as f:
        file_content = parse_csv(f, 
                                 select=['name', 'shares', 'price'], 
                                 types=[str, int, float], 
                                 **opts)
    stocks = [Stock(**row) for row in file_content]
    portfolios = Portfolio(stocks)
    return portfolios

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
    report: Any = []
    report.append(('name', 'Shares', 'Price', 'Change'))
    for stock in portfolio:
        change = prices[stock.name] - stock.price
        report.append((stock.name, f"{stock.shares}", f"{stock.price:0.2f}", f"{change:0.2f}"))
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

def print_report(rawdata: list, formatter: TableFormatter) -> bool:
    '''
    print the report of portfolio
    '''
    header = rawdata[0]
    formatter.heading(header)
    
    for row in rawdata[1:-1]:
        formatter.row(row)
    
    count = rawdata[-1]
    formatter.foot(count)

    return True

def portfolio_report(portfolio: str, prices: str, fmt:str = 'plantext'):
    '''
    read portfolio and prices files, then print the report
    '''
    portfolio_data = read_portfolio(portfolio)
    prices_data = read_prices(prices)
    rawdata = make_report_data(portfolio_data, prices_data)
    formatter = createFormatter(fmt)
    print_report(rawdata, formatter)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        raise SystemExit(f'Usage: python {sys.argv[0]} portfoliofile pricesfile fmt')

    portfolio = sys.argv[1]
    prices = sys.argv[2]
    arguments = [portfolio, prices]
    if len(sys.argv) == 4:
        fmt = sys.argv[3]
        arguments.append(fmt)
    
    portfolio_report(*arguments)
        