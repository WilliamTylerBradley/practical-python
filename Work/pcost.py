# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0

    with open(filename, 'rt') as file:
        reader = csv.reader(file)
        next(reader)
        for stock_info in reader:
            try:
                shares = float(stock_info[1])
                price = float(stock_info[2])
                total_cost = total_cost + shares * price
            except ValueError:
                print('Missing data encountered')

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data\portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost:.2f}')
