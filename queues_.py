#queue


class Queue():
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.self.items)

q = Queue()

q.enqueue("3")
print(q.is_empty())
print(q.items)

        
