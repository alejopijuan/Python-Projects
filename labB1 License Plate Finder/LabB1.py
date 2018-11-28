#!/usr/bin/python3
#Alejo Pijuan

"""This program will be used to search for information about cars given the license plate"""

class Plates:
  """ Class to search information about cars using the license plate as a key"""

  def __init__(self, filename):
    """Opens and reads file and copies to memory"""
    self.number=[]
    f = open(filename, "r")
    for l in f:
      info=l.strip().split('\t')
      self.number.append(info)
    sort_list(self.number)

  def findByPlate(self, LicPlate):
      """Returns the info about the plate"""
      return sortedParts(LicPlate, self.number)



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


def sortedParts(point, l, inleft=0, inright=None):
  if inright==None:
    inright=len(l)
  if inright<inleft+1:
    return None
  middle=(inleft+inright)//2
  if l[middle][0]==point:
    return l[middle][1:]
  if l[middle][0]<point:
    return sortedParts(point, l, middle+1, inright)
  return sortedParts(point, l, inleft, middle)


def sortiter(l,firstinlist,lastinlist):
    if firstinlist<lastinlist:
       splitit = cutit(l,firstinlist,lastinlist)
       sortiter(l,firstinlist,splitit-1)
       sortiter(l,splitit+1,lastinlist)





if __name__ == "__main__":
  filename='sampleplates.txt'
  print('Plates file: {}'.format(filename))
  plates=Plates(filename)
  print("findByPlate('GPA1905')")
  print("Expected answer: ['Chevrolet', 'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers']")
  print("Actual answer: {}".format(plates.findByPlate('GPA1905')))
