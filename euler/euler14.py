'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

'''

def collatz(number, jumps=None):
    if number == 1:
        return jumps
    if jumps is None:
        jumps = 0
    jumps += 1
    if number % 2 == 0:
        return collatz(number/2, jumps)
    else:
        return collatz((number * 3) + 1, jumps)

def collatzcollector(x):
    currentcollatz = 1
    currentnumber = 1
    for number in range(1, x):
        newlatz = collatz(number)
        if newlatz > currentcollatz:
            currentcollatz = newlatz
            currentnumber = number
    return currentnumber
    
print collatzcollector(1000000)
