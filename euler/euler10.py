'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''


def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def populate_primes(primecount):
    primes = [] 
    currentnum = 2
    while len(primes) < primecount:
        if is_prime(currentnum):
            primes.append(currentnum)
        currentnum += 1
    return primes

def populate_prime_values(primemax):
    primes = []
    currentnum = 2
    while currentnum < primemax:
        if is_prime(currentnum):
            primes.append(currentnum)
        currentnum += 1
    return primes

print sum(populate_prime_values(2000000))
