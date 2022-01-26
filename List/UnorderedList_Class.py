from Node_Class import Node

class UnorderedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return not bool(self.head)

    def add(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

    def remove(self, item):
        current = self.head
        previous = None

        while current is not None:
            if current.data == item:
                break
            previous = current
            current = current.next

        if current == self.head:
            self.head = current.next
        elif current is None:
            return f'{item} not in the list'
        else:
            previous.next = current.next

    def __str__(self):
        current = self.head
        list_container = []
        while current is not None:
            list_container.append(str(current))
            current = current.next
        return str(list_container)