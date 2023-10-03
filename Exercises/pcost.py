# read the contents of a file from Data/portfolio.dat
import polars as pl

def read_portfolio(filename):
    portfolio = []
    with open(filename) as file:
        for line in file:
            fields = line.split()
            # try:
            nshares = int(fields[1])
            price = float(fields[2])
            total_cost = nshares * price
            # except ValueError:
            #     print("Bad data: {}".format(line))
            #     continue
            record = {
                'name': fields[0],
                'shares': nshares,
                'price': price,
                'total_cost': round(total_cost, 2)
            }
            portfolio.append(record)
        return portfolio


