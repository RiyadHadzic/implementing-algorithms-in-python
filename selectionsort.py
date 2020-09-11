import math

# this is selection sort.
# It takes input an array of integers of length n
# Going from the kth element to the n-1th element,
# where k starts at the first index
# we go through k+1th element to the nth element and find the smallest one
# the smallest one is now the kth element
# 2 for loops = n^2 run time

array = [13,12,11,1,5,8,3,6]


for x in array:

    key=x
    index=array.index(x)
    posj=index
    for y in array[index+1:len(array)]:
        if y<key:
            key=y
            posj=array.index(y)
    if index!=posj:
        hold=array[index]
        array[index]=key
        array[posj]=hold
print(array)