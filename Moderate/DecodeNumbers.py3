import itertools
import sys
from collections import OrderedDict

encodeMap = OrderedDict([('1', 'A'), ('2', 'B'), ('3', 'C'), ('4', 'D'),
                         ('5', 'E'), ('6', 'F'), ('7', 'G'), ('8', 'H'),
                         ('9', 'I'), ('10', 'J'), ('11', 'K'), ('12', 'L'),
                         ('13', 'M'), ('14', 'N'), ('15', 'O'), ('16', 'P'),
                         ('17', 'Q'), ('18', 'R'), ('19', 'S'), ('20', 'T'),
                         ('21', 'U'), ('22', 'V'), ('23', 'W'), ('24', 'X'),
                         ('25', 'Y'), ('26', 'Z')])

def combos(S, n):
    if (n <= 0): return
    for s in S:
        if len(s) <= n: yield s
        for t in combos(S, n-len(s)): yield s+t

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = line.rstrip()

        candidate = [val for val in encodeMap if val in line]
        collect = []
        for x in combos(candidate, len(line)):
            collect.append(x)
        result = [n for n in collect if n == line]
        print(len(result))
