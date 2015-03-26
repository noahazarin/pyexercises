def is_prime(number):
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

print is_prime(10)
print is_prime(13)

def populate_primes(primecount):
    primes = [] 
    currentnum = 2
    while len(primes) < primecount:
        if is_prime(currentnum):
            primes.append(currentnum)
        currentnum += 1
    return primes

print populate_primes(6)
print populate_primes(100)
print populate_primes(10001)
