import sys

def rwh_primes1(n):
    sieve = [True] * int((n/2))
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int(((n-i*i-1)/(2*i)+1))
    return [2] + [2*i+1 for i in range(1, int(n/2)) if sieve[i]]

path = sys.argv[1]
with open(path, 'r') as inFile:
    for line in inFile:
        line = int(line.rstrip())
        print(",".join(map(str, rwh_primes1(line))))
