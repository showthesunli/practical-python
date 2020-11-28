# pcost.py
#
# Exercise 1.31
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
