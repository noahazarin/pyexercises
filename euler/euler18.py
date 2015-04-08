'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''
list01 = [75]
list02 = [95,64]
list03 = [17,47,82]
list04 = [18,35,87,10]
list05 = [20,04,82,47,65]
list06 = [19,01,23,75,03,34]
list07 = [88,02,77,73,07,63,67]
list08 = [99,65,04,28,06,16,70,92]
list09 = [41,41,26,56,83,40,80,70,33]
list10 = [41,48,72,33,47,32,37,16,94,29]
list11 = [53,71,44,65,25,43,91,52,97,51,14]
list12 = [70,11,33,28,77,73,17,78,39,68,17,57]
list13 = [91,71,52,38,17,14,91,43,58,50,27,29,48]
list14 = [63,66,04,68,89,53,67,30,73,16,69,87,40,31]
list15 = [04,62,98,27,23,9,70,98,73,93,38,53,60,04,23]

bigpyramid = [list01, list02, list03, list04, list05, list06, list07, list08, list09, list10, list11, list12, list13, list14, list15]

minipyramid = [list01, list02, list03]

def pathgen(pathstable, layer, pyramid):
    currentlist = pyramid[layer]
    print "one recursion"
    newpathstable = []
    for path in pathstable:
        pathval = path[0]
        pathloc = path[1]
        if pathloc != len(currentlist) - 1:
            #move up and add new space value
            newpathstable.append([pathval + currentlist[pathloc], pathloc])
        if pathloc != 0:
            #move up and left and add new space value
            newpathstable.append([pathval + currentlist[pathloc-1], pathloc-1])
        if pathloc == len(currentlist) -1 and pathloc == 0:
            newpathstable.append([pathval + currentlist[pathloc], pathloc]) 
    #now go on level up the pyramid, if possible.
    if layer == 0:
        #print newpathstable
        return newpathstable
    else:
        #print newpathstable
        return pathgen(newpathstable, layer-1, pyramid)

g = [[0, b] for b, a in enumerate(list03)]
print pathgen(g, 2, minipyramid)


         
lowestlist = [[0, b] for b, a in enumerate(list15)]
bigpaths = pathgen(lowestlist, 14, bigpyramid)

print bigpaths

highestval = 0
for x in bigpaths:
    if x[0] > highestval:
        highestval = x[0]
print highestval
