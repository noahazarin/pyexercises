'''
reverse an array in place
it's okay to make a placeholder
'''

def reverse_array_in_place(array):
    array = array[:]
    for itemindex in range(0, (len(array))/2):
        space = array[itemindex]
        array[itemindex] = array[-1 * (itemindex+1)]
        array[-1 * (itemindex+1)] = space
    return array

array1 = ["a", "b", "c", "d", "e"]
array2 = ["a", "b", "c", "d", "e", "f"]


print reverse_array_in_place(array1)
print reverse_array_in_place(array1) #make sure that the array being manipulated isnt overwriting input, array1
print reverse_array_in_place(array2)
print reverse_array_in_place(reverse_array_in_place(array1))
