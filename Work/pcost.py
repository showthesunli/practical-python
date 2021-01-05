#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pcost.py
#
# Exercise 4.4
import sys
import csv
from fileparse import parse_csv
from stock import Stock
from report import read_portfolio
from portfolio import Portfolio

def protfolio_cost(name) -> float:
    '''
    Calculate the cost of portfolio
    '''
    stocks = read_portfolio(name)
    portfolio = Portfolio(stocks)
    return portfolio.cost_shares


def main(argv):
    name = sys.argv[1]
    cost = protfolio_cost(name)
    print('Total cost:', cost)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} portfoliodate_file')

    main(sys.argv)