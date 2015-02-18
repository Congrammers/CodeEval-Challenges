def multiOf(n, m):
    return n % m == 0

def primeGen(cap):
    potentPrime = 3
    primeSet = [2, potentPrime]

    while potentPrime < cap:
        # skipping multiple of 2 altogether.
        potentPrime += 2

        primeCount = 0
        for n in primeSet:
            if multiOf(potentPrime, n):
                primeCount += 1
            if primeCount >= 1:
                break

        if primeCount < 1:
            primeSet.append(potentPrime)

    return primeSet

def isPalind(val):
    return str(val) == str(val)[::-1]

def lastPalindPrime():
    primeList = primeGen(1000)
    return next(i for i in reversed(primeList) if isPalind(i))

print(lastPalindPrime())
