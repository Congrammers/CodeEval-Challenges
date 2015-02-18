import sys

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        listing, value = line.rstrip().split(';')
        listing = list(map(int, listing.split(',')))
        value = int(value)

        result = []
        for num in listing:
            delta = value - num
            try:
                if delta == num:
                    raise(ValueError)
                result.append((num, listing.pop(listing.index(delta))))

            except ValueError:
                pass
        if result:
            print(";".join(str(x) + ',' + str(y) for x, y in result))
        else:
            print("NULL")
