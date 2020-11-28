# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                portfolio.append((row[0], int(row[1]), float(row[2])))
            except ValueError as identifier:
                pass
            
    return portfolio

if '__main__' == __name__:
    print(read_portfolio('Data/portfolio.csv'))