import os
import time
from report import read_portfolio

def follow(filename: str):
    f = open(filename, 'rt')
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            continue
        yield line


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv')

    for line in follow('Data/stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

