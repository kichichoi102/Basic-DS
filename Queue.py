class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(1)

    def size(self):
        return len(self.items)


q = Queue()

q.enqueue(3)
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(7)
q.enqueue(9)

print(q.size())


q.dequeue()
q.dequeue()
q.dequeue()

print(q.size())
