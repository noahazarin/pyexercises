'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def add_three_and_five_multiples(top):
    result = 0
    for number in range(1, top+1):
        if number % 3 == 0 or number % 5 == 0:
            result += number
    return result

print add_three_and_five_multiples(999)
