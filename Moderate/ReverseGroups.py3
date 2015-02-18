import itertools
import sys

def chunks(listing, n):
    for i in range(0, len(listing), n):
        yield listing[i:i+n]

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        listing, amount = line.rstrip().split(';')
        listing = listing.split(',')
        amount = int(amount)

        field = list(chunks(listing, amount))
        result = []
        for lis in field:
            if len(lis) == amount:
                result.append(lis[::-1])
            else:
                result.append(lis)

        print(",".join(itertools.chain.from_iterable(result)))
