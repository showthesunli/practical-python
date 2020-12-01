#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pcost.py
#
# Exercise 2.16
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

if len(sys.argv) == 2:
    name = sys.argv[1]
else:
    name = 'Data/portfoliodate.csv'

cost = protfolio_cost(name)
print('Total cost:', cost)