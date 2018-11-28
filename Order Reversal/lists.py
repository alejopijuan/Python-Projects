#! /usr/bin/env python3
# Alejo Pijuan  
# 10/27/16
# Create some mathematical functions

intListOne = [0,1,2,3,4]
intListTwo = [4,3,2,1,0]
intList = [1,2,3,4,5,6]

def main():
    print(productOfEven(intList))
    print(sumOfOdd(intList))
    print(oddMembers(intList))
    print(changeList(intList))
    print(isReverse(intListOne, intListTwo))


def productOfEven(intList):
    product = 1
    for i in intList:
        if i%2==0:
            product = product*i
    return product
        

def sumOfOdd(intList):
    summ = 0
    for i in intList:
        if i%2!=0:
            summ = summ+i
    return summ
    
def oddMembers(intList):
    newList = []
    for i in intList:
        if i%2!=0:
            newList.append(i)
    return newList
    
def changeList(intList):
    for i in range(len(intList)):
        if intList[i]%2==0:
            intList[i] = intList[i]//2
        else:
            intList[i] = (intList[i]+4)*2
    return intList
        
def isReverse(intListOne, intListTwo):
    intListOne.reverse()
    return intListOne == intListTwo
    



    
if __name__ == "__main__":
    main()
