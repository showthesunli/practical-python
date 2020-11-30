# report.py
#
# Exercise 2.7
import csv
import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                portfolio.append({'name':row[0],
                 'shares':int(row[1]), 'price':float(row[2])})
            except ValueError as identifier:
                pass
            
    return portfolio

def read_prices(filename):
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

if '__main__' == __name__:
    # print(read_portfolio('Data/portfolio.csv'))
    # print(read_portfolio('Data/portfolio.csv'))
    # print(read_prices('Data/prices.csv'))
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    intres = 0.00
    for i in portfolio:
        intres_of_one_share = prices[i['name']]*i['shares'] - i['shares']*i['price']
        intres += intres_of_one_share
    print('total gain is', intres)