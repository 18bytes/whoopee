"""
A simple Queue implementation in Python.
FIFO
"""
class Queue:
    def __init__(self):
        self.data = []

    def poll(self):
        result = self.peek()
        del self.data[0]
        return result

    def peek(self):
        size = len(self.data)
        if size > 0:
            return self.data[0]
        else:
            raise Exception("No data in Queue")

    def offer(self, elem):
        self.data.append(elem)

    def get_data(self):
        return self.data

if __name__ == "__main__":
    queue = Queue()
    queue.offer(22)
    queue.offer(33)
    print    queue.poll()
    print    queue.poll()
    print queue.get_data()
