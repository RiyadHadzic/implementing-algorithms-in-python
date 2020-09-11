import math
import sys

def partition(array,lIdx,rIdx):
    position=array[rIdx]
    i=0
    j=0

    while j<rIdx:
        if array[j]>position:
            j=j+1
        else:
            hold=array[i]
            array[i]=array[j]
            array[j]=hold
            i=i+1
            j=j+1

    hold=array[i]
    array[i]=position
    array[rIdx]=hold

    return i

def quicksort(array,lIdx,rIdx):
    print(array)
    if lIdx<rIdx:
        partitionIdx= partition(array,lIdx,rIdx)
        quicksort(array,lIdx,partitionIdx-1)
        quicksort(array,partitionIdx+1,rIdx)

# after this point, I'm just testing if the algorithm works or not
# it appears to work for the array arr=[19,10,1,5,31,21]

arr=[19,10,1,5,31,21]

quicksort(arr,0,len(arr)-1)

def checkSorted(anArray):
    arrayidx=0
    x=1
    while arrayidx!=len(arr)-1:
        if anArray[arrayidx]<=anArray[arrayidx+1]:
            arrayidx=arrayidx+1
        else:
            x=-1
    if x==-1:
        print('not sorted')
    else:
        print('sorted')

checkSorted(arr)

## it appears to work for arr=[-1,-2,-3,-4,-5] as well.

arr=[-1,-2,-3,-4,-5]
quicksort(arr,0,len(arr)-1)
checkSorted(arr)

# one last test, it appears to work for arr=[-1,1,-1,1,-1,1] as well
arr=[-1,1,-1,1,-1,1]
quicksort(arr,0,len(arr)-1)
checkSorted(arr)
