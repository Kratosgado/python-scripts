
def checkPrime(number):
    factors = 0
    for i in range(2, number+1, 1):
        if (number % i == 0):
            factors += 1
        if (factors > 1):
            return 0
    if (factors == 1):
        return number
    return 0


def getPrimes(prime):
    primes = []
    for i in range(2, prime, 1):
        primes.append(checkPrime(i)) if (checkPrime(i) == i) else ""
    return primes


def getConsecutivePrimeSum(prime):

    primes = getPrimes(prime)
    sum = 0
    for i in range(len(primes)-1):
        sum += primes[i]
        if (sum == prime):
            return sum
        if (sum > prime):
            return


print(getConsecutivePrimeSum(963))
# for i in range(901, 1000, 2):
#     print(".", end="")
#     if (checkPrime(i) == i):
#         print(getConsecutivePrimeSum(i))
