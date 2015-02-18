import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        trash, listing = line.rstrip().split(';')
        listing = list(map(int, listing.split(',')))
        print(sum(listing) - sum(set(listing)))
