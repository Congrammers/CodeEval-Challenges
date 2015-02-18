import sys

roman_numeral_map = (('M', 1000),
                     ('CM', 900),
                     ('D', 500),
                     ('CD', 400),
                     ('C', 100),
                     ('XC', 90),
                     ('L', 50),
                     ('XL', 40),
                     ('X', 10),
                     ('IX', 9),
                     ('V', 5),
                     ('IV', 4),
                     ('I', 1))

def to_roman(n):
    result = ''
    for numeral, integer in roman_numeral_map:
        multi = int(n / integer)
        result += multi*numeral
        n -= multi*integer
    return result

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        print(to_roman(int(line.rstrip())))
