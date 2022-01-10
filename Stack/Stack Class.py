class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return not bool(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


# Reversing a string using Stack Class
def rev_string(my_str):
    answer = Stack()
    for letter in my_str:
        answer.push(letter)
    rev_ans = ''
    while not answer.is_empty():
        rev_ans += answer.pop()

    return rev_ans


print(rev_string('asdfghjkl'))
