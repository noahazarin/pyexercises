'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def extractgreatestprime(largenum, currentlargestfactor=1):
    #normally would use: for potentialfactor in range(2, largenum+2/2)
    #memory error. while loop iterates until recursion which is less
    #space intensive
    potentialfactor = 2
    while potentialfactor < largenum+2/2:
        if largenum % potentialfactor == 0:
            newresultnum = largenum / potentialfactor
            if potentialfactor > currentlargestfactor:
                currentlargestfactor = potentialfactor
            return extractgreatestprime(newresultnum, currentlargestfactor)
        potentialfactor += 1
    return currentlargestfactor

print extractgreatestprime(13195)
print extractgreatestprime(600851475143)
