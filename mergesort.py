import math
import sys

#first we need a method that merges 2 sorted arrays
#method merge takes 2 sub arrays, one from b to m,
#where m is the cieiling of (t+b)/2
def merge(returnSortedArray,smaller,mid,bigger):

    if smaller==bigger:
        return
    leftArray=[]
    rightArray=[]

    for x in range(smaller,mid+1):
        leftArray.append(returnSortedArray[x])
    for x in range(mid+1,bigger+1):
        rightArray.append(returnSortedArray[x])

    i = 0
    j = 0
    counter=smaller
    while ((i!=len(leftArray)) and (j!=len(rightArray))):
        if leftArray[i]<=rightArray[j]:
            returnSortedArray[counter]=leftArray[i]
            i=i+1
            counter=counter+1
        else:
            returnSortedArray[counter]=rightArray[j]
            j=j+1
            counter=counter+1
    if i==len(leftArray):
        while j!=len(rightArray):
            returnSortedArray[counter]=rightArray[j]
            counter=counter+1
            j=j+1
    else:
        while i!=len(leftArray):
            returnSortedArray[counter]=leftArray[i]
            counter=counter+1
            i=i+1
    return returnSortedArray

#this is mergesort
def mergesort(unsortedArray,leftidx,rightidx):
    midpt=math.floor((leftidx+rightidx)/2)

    if leftidx<rightidx:
        mergesort(unsortedArray,leftidx,midpt)
        mergesort(unsortedArray,midpt+1,rightidx)
        merge(unsortedArray,leftidx,midpt,rightidx)
    return unsortedArray

lol=[10,9,8,7,6]
print(mergesort(lol,0,len(lol)-1))