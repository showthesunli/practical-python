#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# pcost.py
#
# Exercise 3.18
import sys
import csv
from fileparse import parse_csv

def protfolio_cost(name):
    '''
    Calculate the cost of portfolio
    '''
    with open(name, 'rt') as f:
        rows = parse_csv(f ,types=[str, int, float], select=['name', 'shares', 'price'])
        
        cost = 0
        for row in rows:
            cost += row['shares']*row['price']
            
    return cost


def main(argv):
    name = sys.argv[1]
    cost = protfolio_cost(name)
    print('Total cost:', cost)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} portfoliodate_file')

    main(sys.argv)