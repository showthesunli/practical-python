#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pcost.py
#
# Exercise 3.15
import sys
import csv

def protfolio_cost(name):
    '''
    Calculate the cost of portfolio
    '''
    with open(name, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        cost = 0
        for row in rows:
            record = dict(zip(header, row))
            try:
                shares = int(record['shares'])
                price = float(record['price'])
                cost += shares*price
            except ValueError as identifier:
                print('Waring Can\'t parse', row)
            
    return cost


def main(argv):
    name = sys.argv[1]
    cost = protfolio_cost(name)
    print('Total cost:', cost)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} portfoliodate_file')

    main(sys.argv)