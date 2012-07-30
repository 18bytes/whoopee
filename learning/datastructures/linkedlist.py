import unittest

class Entry():

  def __init__(self, prev, obj, next):
    self.previous = prev
    self.content = obj
    self.next = next

  def __init__(self):
    self.previous = None
    self.content = None
    self.next = None


class LinkedList():

  def __init__(self):
    self.__size = 0
    self.first = None
    self.last  = None

  def addFirst(self, obj):
    if self.__size is 0:
      self.first = Entry(None, obj, None)
      self.last  = self.first
    else:
      newEntry            = Entry(None, obj, self.first)
      self.first.previous = newEntry
      self.first          = newEntry

    self.__size += 1
    
  def addLast(self, obj):
    entry = self.addBefore(obj, self.header)
  
  def getFirst(self):
    pass

  def getLast(self):
    pass

  def removeFirst(self):
    pass

  def removeLast(self):
    pass

  def remove(self, obj):
    pass

  def add(self, obj):
    pass

  def getEntryAt(self, pos):
    pass

  def addBefore(self, obj, entry):
    newEntry = Entry(entry.previous, obj, entry)
    newEntry.previous.next = newEntry
    newEntry.next.previous = newEntry
    self.__size = self.__size + 1

    return newEntry

  def clear(self):
    self.__size = 0
    self.header.next = self.header.previous = self.header
    pass

  def getSize(self):
    return self.__size

class LinkedListTest(unittest.TestCase):
  
  def setUp(self):
    self.linkedlist = LinkedList()

  def test_add(self):
    size = self.linkedlist.getSize()
    self.linkedlist.add('test')
    self.assertEquals(size + 1, self.linkedlist.getSize())

  def test_clear(self):
    self.linkedlist.add('some')
    self.assertEquals(size, 0)
    self.assertEquals(self.linkedlist.header.previous, self.linkedlist.header)
    self.assertEquals(self.linkedlist.header.next, self.linkedlist.header)
  

if __name__ == '__main__':
  suite = unittest.TestLoader().loadTestsFromTestCase(LinkedListTest)
  unittest.TextTestRunner(verbosity=2).run(suite)
