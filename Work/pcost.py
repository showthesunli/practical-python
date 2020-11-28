#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# pcost.py
#
# Exercise 1.33
import sys

def protfolio_cost(name):
    with open(name, 'rt') as f:
        next(f)
        cost = 0
        for line in f:
            row = line.split(',')
            try:
                cost = cost+ int(row[1])* float(row[2])
            except ValueError as identifier:
                print('Waring Can\'t parse', line)
            
    return cost

if len(sys.argv) == 2:
    name = sys.argv[1]
else:
    name = 'Data/portfolio.csv'

cost = protfolio_cost(name)
print('Total cost:', cost)