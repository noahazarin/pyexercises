'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

#let's try populating a 2-d array and finding the largest number

products=[]
for x in range(0, 1000):
    products.append([])
    for y in range(0, 1000):
        products[x].append(x*y)

outprod = 9009
for row in products:
    for item in row:
        stritem = str(item)
        for spot in range(0,(len(stritem)/2)):
            if stritem[spot] != stritem[(spot * -1) -1]:
                item = 0
        if item > outprod:
            outprod = item

print outprod


