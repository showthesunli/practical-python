# report.py
#
# Exercise 2.16
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
                print(record)
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

def make_report(portfolio: list, prices: dict) -> list:
    report = []
    report.append(('name', 'Shares', 'Price', 'Change'))
    for i in portfolio:
        change = prices[i['name']] - i['price']
        report.append((i['name'], i['shares'], i['price'], change))
    return report

if '__main__' == __name__:
    # print(read_portfolio('Data/portfolio.csv'))
    # print(read_portfolio('Data/portfolio.csv'))
    # print(read_prices('Data/prices.csv'))
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')

    intres = 0.00
    total_cost = 0.00
    for i in portfolio:
        cost_of_one_share = i['shares']*i['price']
        intres_of_one_share = prices[i['name']]*i['shares'] - cost_of_one_share
        total_cost += cost_of_one_share

    print('total cost is', total_cost)

    print('total gain is', intres)

    print(make_report(portfolio, prices))