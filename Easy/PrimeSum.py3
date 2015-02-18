def multiOf(n, m):
    return n % m == 0

def primeGen(maxLen):
    potentPrime = 3
    primeSet = [2, potentPrime]

    while len(primeSet) < maxLen:
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

print(sum(primeGen(1000)))
