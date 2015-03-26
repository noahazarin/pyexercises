def get_sum(numberlist):
    result = 0
    for x in numberlist:
        result += x
    return result

def make_squares(numberlist):
    result = []
    for x in numberlist:
        result.append(x**2)
    return result


#print get_sum([10, 1, 2, 3, 4])
#print make_squares([1, 2, 3, 4, 5, 6])

def squaresum_minus_sumofsquares(topnumber):
    numberlist = []
    for x in range(1, topnumber+1):
        numberlist.append(x)
    sum_of_squares = get_sum(make_squares(numberlist))
    square_of_sum = get_sum(numberlist) ** 2
    return square_of_sum - sum_of_squares

print squaresum_minus_sumofsquares(100)
