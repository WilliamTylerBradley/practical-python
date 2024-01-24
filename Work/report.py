# report.py
#
# Exercise 2.4
import csv

def portfolio_cost(filename):
    '''Computes the total cost (shares*price) of a portfolio file'''
    total_cost = 0.0

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2])
            total_cost += nshares * price
    return total_cost

def read_portfolio(filename):
    '''Reads in a portfolio file'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            holding = {'name':row[0], 
                       'shares':int(row[1]),
                        'price':float(row[2])}
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if row:
                prices[row[0]] = float(row[1])
    return prices

def make_report(portfolio, prices):
    report = []
    for stock in portfolio:
        row = (stock['name'], stock['shares'], prices[stock['name']], prices[stock['name']] - stock['price'])
        report.append(row)
    return report

portfolio = read_portfolio('Data\portfolio.csv')
prices = read_prices('Data\prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))

for name, shares, price, change in report:
    print(f'{name:>10s} {shares:>10d} {f"${price:.2f}":>10s} {change:>10.2f}')