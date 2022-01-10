from Stack_Class import Stack


def base_converter(decimal_num, base):
    digits = '0123456789ABCDEF'  # Max is base-16
    remainder_stack = Stack()

    while decimal_num > 0:
        remainder = decimal_num % base
        remainder_stack.push(remainder)
        decimal_num = decimal_num // base

    answer = ''
    while not remainder_stack.is_empty():
        answer += digits[remainder_stack.pop()]

    return answer


print(base_converter(123, 2))
print(base_converter(123, 16))
print(base_converter(31231231231, 16))
