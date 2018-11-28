#!/usr/bin/python3

'''this program will look through a list looking for an entry that mathes the value
'''
def hunt(alist, avalue):
    '''the function will use binary search to find the value'''
    firstvalue = 0
    lastvalue = len(alist)
    while firstvalue < lastvalue: 
        middle = firstvalue + (lastvalue - firstvalue) // 2
        val = alist[middle]
        if avalue == val:
            return middle
        elif avalue > val:
            if firstvalue == middle:  
                break      
            firstvalue = middle
        elif avalue < val:
            lastvalue = middle



if __name__ == "__main__":
    print('Test: hunt([1,2,3], 2)')
    print('Expected answer: 1')
    location=hunt([1,2,3], 2)
    print('Actual answer: {}'.format(location))
