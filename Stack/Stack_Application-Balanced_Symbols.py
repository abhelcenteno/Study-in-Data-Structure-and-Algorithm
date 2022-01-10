from Stack_Class import Stack


def sym_checker(sym_str):
    sym_container = Stack()
    for symbol in sym_str:
        if symbol in '([{':  # will check if opening symbols will be pushed
            sym_container.push(symbol)
        else:
            if sym_container.is_empty():  # if symbol container is empty and upcoming symbol is ')]}' meaning
                # it is automatically unbalanced
                return False
            else:
                if not partner_check(sym_container.pop(), symbol):  # check if symbols are partners
                    return False

    return sym_container.is_empty()


def partner_check(symbol1, symbol2):
    opening = '([{'
    closing = ')]}'
    return opening.index(symbol1) == closing.index(symbol2)


print(sym_checker('()()(([]{}))([])()'))
print(sym_checker('(()()(([]{}))([])()'))
print(sym_checker(')('))
