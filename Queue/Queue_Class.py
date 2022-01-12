class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def is_empty(self):
        return not bool(self._items)

    def size(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)


# q = Queue()
# q.enqueue('asd')
# q.enqueue(123)
# print(q.size())
# print(q.is_empty())
# print(q)
