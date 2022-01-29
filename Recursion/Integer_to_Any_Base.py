def int_to_binary(n):
    if n // 2 == 0:
        return str(n)
    else:
        return int_to_binary(n // 2) + str(n % 2)


def int_to_any_base(num, base):  # max is base 16
    convert_str = '0123456789ABCDEF'
    if num // base == 0:
        return convert_str[num]
    else:
        return int_to_any_base(num // base, base) + convert_str[num % base]
