#!/usr/bin/python3
#Alejo Pijuan

"""Program that returns the extra information known about the car in a list of strings"""

class Plates:
  """Get info about the plate and process it"""

  
  def __init__(self, filename):
    """Read the file and split each word """
    
    self.number={}
    f = open(filename, "r")
    for l in f:
        info=l.strip().split('\t')
        self.number[info[0]]=info[1:]
        
  def findByPlate(self, plate):
    """Find the plate and return None if not found"""
    
    try:
      return self.number[plate]
    except KeyError:
      return None



if __name__ == "__main__":
  filename='sampleplates.txt'
  print('Plates file: {}'.format(filename))
  plates=Plates(filename)
  print("findByPlate('GPA1905')")
  print("Expected answer: ['Chevrolet', 'Corvette Coupe', '2008', 'pink', 'Sylvia Cheers']")
  print("Actual answer: {}".format(plates.findByPlate('GPA1905')))
