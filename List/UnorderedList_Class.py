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

    def append(self, item):
        current = self.head
        previous = None
        while current is not None:
            previous = current
            current = current.next
        previous.next = Node(item)

    def index(self, item):
        current = self.head
        count = 0
        while current is not None:
            if current.data == item:
                return count
            current = current.next
            count += 1

    def insert(self, item, pos):
        current = self.head
        previous = None
        count = 0
        if self.head is None:
            self.add(Node(item))
            return f'This is the first item in the list; position {pos} is disregarded'
        if pos > self.size():
            return f'Kindly specify position from 0 to {self.size()}'
        while current is not None:
            if count == pos:
                if count == 0:
                    temp = Node(item)
                    temp.next = self.head
                    self.head = temp
                else:
                    temp = Node(item)
                    temp.next = current
                    previous.next = temp
            count += 1
            previous = current
            current = current.next
        previous.next = Node(item)

    def pop(self, pos=None):
        current = self.head
        previous = None
        counter = 0
        if current is None:
            return 'There is currently no item in the list'
        if pos is None or pos == (self.size() - 1):
            while current.next is not None:
                previous = current
                current = current.next
                counter += 1
            previous.next = None
            return current.data
        else:
            if pos >= self.size():
                return f'Kindly specify position from 0 to {self.size()-1}'
            if pos == 0:
                previous = self.head
                self.head = self.head.next
                return previous.data
            while counter != pos:
                previous = current
                current = current.next
                counter += 1
            previous.next = current.next
            return current.data

    def reverse(self):
        if self.head is None:
            return None
        current = self.head
        previous = None
        next = None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def __str__(self):
        current = self.head
        list_container = []
        while current is not None:
            list_container.append(str(current))
            current = current.next
        return str(list_container)

ulist1 = UnorderedList()
ulist1.add(1)
ulist1.add(2)
ulist1.add(3)
ulist1.add(4)
ulist1.add(5)
ulist1.add(6)
ulist1.add(7)
print(ulist1)

ulist2 = UnorderedList()
ulist2.add('a')
ulist2.add('b')
ulist2.add('c')
# ulist2.add('d')
# ulist2.add('e')
print(ulist2)

def zip_list(list1, list2):
    head = list1
    tail = list1
    current1 = list1.next
    current2 = list2
    counter = 0

    while current1 is not None and current2 is not None:
        if counter % 2 == 0:
            tail.next = current2
            tail = current2
            current2 = current2.next
        else:
            tail.next = current1
            tail = current1
            current1 = current1.next
        counter += 1

    if current1 is None:
        tail.next = current2
    elif current2 is None:
        tail.next = current1


    current = head
    list_container = []
    while current is not None:
        list_container.append(str(current))
        current = current.next
    return str(list_container)

print(zip_list(ulist1.head, ulist2.head))