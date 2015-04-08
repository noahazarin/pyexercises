def factorial(number):
    result = 1
    for x in range(1, number+1):
        result *= x
    return result

def sumdigits(number):
    result = 0
    for strdigit in str(number):
        result += int(strdigit)
    return result

print sumdigits(factorial(10))
print sumdigits(factorial(100))
