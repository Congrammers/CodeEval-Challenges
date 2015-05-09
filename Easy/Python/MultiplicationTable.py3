multiply = lambda x, y: x * y
multitable = [[multiply(i, j) for i in range(1, 13)] for j in range(1, 13)]

for row in multitable:
    print('{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}'
          '{:>4}{:>4}{:>4}'.format(*row))
