import sys

def rwh_primes1(m, n):
    sieve = [True] * int((n/2))
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int(((n-i*i-1)/(2*i)+1))
    result = [2] + [2*i+1 for i in range(1, int(n/2)) if sieve[i]]
    return [v for v in result if v >= m]

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        start, end = map(int, line.rstrip().split(','))
        print(len(rwh_primes1(start, end+1)))
