#!/usr/bin/python3

""" Demonstrate simple linked list growth. """

class LinkedList:
  """ LinkedList provides a linked list.

      The user can get the current length of the list, get the item
      stored at any valid index, or insert a new item at a specified index.
      Items can be inserted into the LinkedList until the computer memory
      is exhausted.
  """
  
  def __init__(self):
    """ Initialize an empty linked list. """
    self.behind=LinkedNode(None)
    self.front=LinkedNode(None,self.behind)
    self.final=self.front
    self.length=0



    
  def __len__(self):
    """ Returns the number of items in the LinkedList. """
    return self.length

    
  def getNode(self, idx):
    """ Returns the node before index idx.
        Raises an IndexError if the idx is invalid.
    """
    idx=self.validateAccess(idx)
    node=self.front
    for i in range(idx):
      node=node.link
    return node

  
  def __getitem__(self, idx):
    """ Returns the item at index idx.
        Raises an IndexError if the idx is invalid.
    """
    return self.getNode(idx).link.data

  
  def append(self, item):
    """ Add the floating point number item to the end of the list.
        The capacity is doubled if there is not otherwise room to add item.
    """
    node=LinkedNode(item, self.behind)
    self.final.link=node
    self.final=node
    self.length+=1

    
  def validateInsert(self, idx):
    """ Returns a normalized form of idx if idx is valid for insert.
        Raise an IndexError if idx is invalid.
    """
    if idx<0 or idx>self.length:
      raise IndexError
    return idx

  
  def validateAccess(self, idx):
    """ Returns a normalized form of idx if idx is valid for access.
        Raise an IndexError if idx is invalid.
    """
    if idx<-1 or idx>=self.length:
      raise IndexError
    return idx

  
  def insert(self, idx, item):
    """ Inserts the floating point number item at idx.
        Raises an IndexError if the idx is invalid.
    """
    if idx==self.length:
      return self.append(item)
    insert=self.getNode(self.validateInsert(idx))
    node=LinkedNode(item, insert.link)
    insert.link=node
    self.length+=1

    
  def __str__(self):
    """ Return the number of items in the linked list."""
    out=""
    sep=""
    node=self.front.link
    while node!=self.behind:
      out=out + sep + str(node.data)
      sep=", "
      node=node.link
    return out


class LinkedNode:
  def __init__(self, data, link=None):
    self.data=data
    self.link=link

    

if __name__ == "__main__":
  sample=LinkedList()
  print("len(sample)")
  print("  Expected: 0")
  print("  Actual: {}".format(len(sample)))

  sample.insert(0, 0.7879183363699951)
  print('sample.insert(0, 0.7879183363699951)')
  sample.insert(1, 0.8249938154876826)
  print('sample.insert(1, 0.8249938154876826)')
  sample.insert(0, 0.41979511664048086)
  print('sample.insert(0, 0.41979511664048086)')
  sample.insert(2, 0.38311278079429256)
  print('sample.insert(2, 0.38311278079429256)')
  sample.insert(0, 0.02615745603398889)
  print('sample.insert(0, 0.02615745603398889)')
  sample.insert(0, 0.9096667329241896)
  print('sample.insert(0, 0.9096667329241896)')
  sample.insert(5, 0.5775226870686715)
  print('sample.insert(5, 0.5775226870686715)')
  sample.insert(6, 0.08178455962969056)
  print('sample.insert(6, 0.08178455962969056)')
  sample.insert(0, 0.8794845298926424)
  print('sample.insert(0, 0.8794845298926424)')
  sample.insert(7, 0.7065827932270193)
  print('sample.insert(7, 0.7065827932270193)')

  print("len(sample)")
  print("  Expected: 10")
  print("  Actual: {}".format(len(sample)))

  print('sample[6]')
  print('  Expect: 0.5775226870686715')
  print('  Actual: {}'.format(sample[6]))
  print('sample[8]')
  print('  Expect: 0.08178455962969056')
  print('  Actual: {}'.format(sample[8]))
  print('sample[0]')
  print('  Expect: 0.8794845298926424')
  print('  Actual: {}'.format(sample[0]))
