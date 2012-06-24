

class Entry():

  def __init__(self, prev, obj, next):
    self.previous = prev
    self.content = obj
    self.next = next


class LinkedList():

  def __init__(self):
    self.size = 0
    self.pointer = Entry()
    self.pointer.next = self.pointer.previous = self.pointer


  def addFirst(self, obj):
    entry = self.addBefore()

  def addLast(self, obj):
    entry = self.addBefore(obj, self.pointer)
  
  def getFirst(self):
  def getLast(self):
  def removeFirst(self):
  def removeLast(self):
  def remove(self, obj):
  def add(self):
  def getEntryAt(self, pos):

  def addBefore(self, obj, entry):
    newEntry = Entry(entry.previous, obj, entry)
    newEntry.previous.next = newEntry
    newEntry.next.previous = newEntry
    size = size + 1

    return newEntry