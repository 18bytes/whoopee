"""
  A simple stack implementation in Python.
"""
class Stack:
    def __init__(self, mx_size):
        self.data = []
        self.max_size = mx_size
    
    def push(self, val):
        size = len(self.data)
        if size >= self.max_size:
            raise Exception("Stackoverflow error!!")
        self.data.append(val)
    
    def peek(self):
        size = len(self.data)
        if size == 0:
            raise Exception("Stackunderflow error!!")
        result = self.data[size-1]
        return result

    def pop(self):
        size   = len(self.data)
        result = self.peek()
        del(self.data[size-1])
        return result

    def get_data(self):
        return self.data

    def is_empty(self):
        return (len(self.data) == 0)

if __name__ == "__main__":
    stack = Stack(20)
    stack.push(22)
    stack.push(33)
    stack.push(44)


    print stack.pop()
    print stack.pop()
    print stack.pop()
    print stack.get_data()
    print stack.get_data()
    print "Hello"
