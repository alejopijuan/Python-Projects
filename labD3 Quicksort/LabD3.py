#!/usr/bin/python3
'''implement quicksort to sort the items in the list'''
def sort_list(l):
    """sort the list in backwards alphabetical order """
    sortiter(l,0,len(l)-1)

def cutit(l,firstinlist,lastinlist):
   thepivot = l[firstinlist]
   left = firstinlist+1
   right = lastinlist
   done = False
   while not done:
       while left <= right and l[left] <= thepivot:
           left = left + 1
       while l[right] >= thepivot and right >= left:
           right = right -1
       if right < left:
           done = True
       else:
           temporal = l[left]
           l[left] = l[right]
           l[right] = temporal

   temporal = l[firstinlist]
   l[firstinlist] = l[right]
   l[right] = temporal
   return right



def sortiter(l,firstinlist,lastinlist):
    if firstinlist<lastinlist:
       splitit = cutit(l,firstinlist,lastinlist)
       sortiter(l,firstinlist,splitit-1)
       sortiter(l,splitit+1,lastinlist)


if __name__ == "__main__":
    l=["the", "cat", "in", "the", "hat", "is", "back"]
    print('sort_list({})'.format(l));
    print("Expected answer: ['back', 'cat', 'hat', 'in', 'is', 'the', 'the']")
    sort_list(l);
    print('Actual answer: {}'.format(l))
