import math

#Implementation of binary search

def binarysearch(sortedArray,searchfor):
    v=searchfor
    i=0
    j=len(sortedArray)-1
    x=math.floor((i+j)/2)
    timecounter=0
    print('current idx: ', x)
    while sortedArray[x]!=v:
        if sortedArray[x]<v:
            if sortedArray[x+1]==v:
                x=x+1
                timecounter=timecounter+1
                print('current idx: ',x)
                break
            i=x
            x=math.floor((i+j)/2)
            print('current idx: ',x)
            timecounter=timecounter+1
        else:
            j=x
            x = math.floor((i + j) / 2)
            print('current idx: ',x)
            timecounter=timecounter+1
    print(timecounter)
    return x

array=[1,5,7,8,9,10,11,12,13,14,15]

print(binarysearch(array,15))