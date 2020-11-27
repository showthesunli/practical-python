# pcost.py
#
# Exercise 1.30
def protfolio_cost(name):
    with open(name, 'rt') as f:
        next(f)
        cost = 0
        for line in f:
            row = line.split(',')
            cost = cost+ int(row[1])* float(row[2])
    return cost
