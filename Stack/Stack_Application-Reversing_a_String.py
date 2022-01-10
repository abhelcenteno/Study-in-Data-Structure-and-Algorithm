from Stack_Class import Stack


def rev_string(my_str):
    answer = Stack()
    for letter in my_str:
        answer.push(letter)
    rev_ans = ''
    while not answer.is_empty():
        rev_ans += answer.pop()

    return rev_ans


print(rev_string('the quick brown fox'))
