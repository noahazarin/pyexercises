'''

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.


'''
def split_thousand(number):
    hundreds = number / 100
    tens = (number / 10) % 10
    ones = (number % 100) % 10
    return [hundreds, tens, ones]

def digit_to_word(digit):
    if digit == 0:
        return ""
    elif digit == 1:
        return "one"
    elif digit == 2:
        return "two"
    elif digit == 3:
        return "three"
    elif digit == 4:
        return "four"
    elif digit == 5:
        return "five"
    elif digit == 6:
        return "six"
    elif digit == 7:
        return "seven"
    elif digit == 8:
        return "eight"
    elif digit == 9:
        return "nine"
    else:
        return "digit not found"

def wordify_number_list(numberlist):
    hundreds = numberlist[0]
    tens = numberlist[1]
    ones = numberlist[2]
    outstring = ""
    if hundreds == 10:
        return "OneThousand"
    elif hundreds != 10:
        outstring += digit_to_word(hundreds)
        if len(outstring) > 0:
            outstring += "hundred"
            if tens != 0 or ones != 0:
                outstring += "and"
    if tens == 2:
        outstring += "twenty"
        outstring += digit_to_word(ones)
    elif tens == 3:
        outstring += "thirty"
        outstring += digit_to_word(ones)
    elif tens == 4:
        outstring += "forty"
        outstring += digit_to_word(ones)
    elif tens == 5:
        outstring += "fifty"
        outstring += digit_to_word(ones)
    elif tens == 6:
        outstring += "sixty"
        outstring += digit_to_word(ones)
    elif tens == 7:
        outstring += "seventy"
        outstring += digit_to_word(ones)
    elif tens == 8:
        outstring += "eighty"
        outstring += digit_to_word(ones)
    elif tens == 9:
        outstring += "ninety"
        outstring += digit_to_word(ones)
    elif tens == 0:
        outstring += digit_to_word(ones)
    elif tens == 1:
        if ones == 0:
            outstring += "ten"
        elif ones == 1:
            outstring += "eleven"
        elif ones == 2:
            outstring += "twelve"
        elif ones == 3:
            outstring += "thirteen"
        elif ones == 4:
            outstring += "fourteen"
        elif ones == 5:
            outstring += "fifteen"
        elif ones == 6:
            outstring += "sixteen"
        elif ones == 7:
            outstring += "seventeen"
        elif ones == 8:
            outstring += "eighteen"
        elif ones == 9:
            outstring += "nineteen"
    return outstring


print wordify_number_list(split_thousand(435))
print wordify_number_list(split_thousand(100))
print wordify_number_list(split_thousand(10))
print wordify_number_list(split_thousand(13))
print wordify_number_list(split_thousand(215))
print wordify_number_list(split_thousand(618))
print wordify_number_list(split_thousand(180))
print wordify_number_list(split_thousand(604))
print wordify_number_list(split_thousand(3))


length = 0
for x in range (1, 1001):
    length += len(wordify_number_list(split_thousand(x)))
    print wordify_number_list(split_thousand(x))

print length
