# report.py
#
# Exercise 3.2
import csv
import pprint

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
    report.append({'intres': intres, 'totcal_cost': total_cost})
    return report

def portfolio_report(portfolio: str, prices: str) -> list:
    '''
    read portfolio and prices files, then print the report
    '''
    portfolio = read_portfolio(portfolio)
    prices = read_prices(prices)

    report = print_report(portfolio, prices)
    
    print(report)
    return report