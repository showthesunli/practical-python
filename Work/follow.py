import os
import time

def follow(filename):

    f = open(filename)
    f.seek(0, os.SEEK_END)
    while True:
        line = f.readline()
        if line == '':
            continue
        yield line


if __name__ == '__main__':
    it = follow('Data/stocklog.csv')
    for line in it:
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change<0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

