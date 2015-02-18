import sys
from collections import OrderedDict

cashDict = OrderedDict([(10000, "ONE HUNDRED"),
                        (5000, "FIFTY"),
                        (2000, "TWENTY"),
                        (1000, "TEN"),
                        (500, "FIVE"),
                        (200, "TWO"),
                        (100, "ONE"),
                        (50, "HALF DOLLAR"),
                        (25, "QUARTER"),
                        (10, "DIME"),
                        (5, "NICKEL"),
                        (1, "PENNY")])

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        purcPrice, cash = map(float, line.rstrip().split(';'))
        purcPrice = int(100*purcPrice)
        cash = int(100*cash)
        delta = cash - purcPrice

        if (delta < 0):
            print("ERROR")
            continue
        if (delta == 0):
            print("ZERO")
            continue

        result = []
        for val in cashDict:
            while delta != 0:
                if val > delta:
                    break
                delta -= val
                result.append(cashDict[val])
        print(",".join(result))
