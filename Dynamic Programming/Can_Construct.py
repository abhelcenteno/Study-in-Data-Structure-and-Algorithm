def can_construct(target, char_list, memo={}):
    if target == '':
        return True

    if target in memo:
        return memo[target]

    for char in [x for x in char_list if len(x) <= len(target)]:
        if target.startswith(char):
            remaining = target[len(char):]
            if can_construct(remaining, char_list, memo) is True:
                return True

    memo[target] = False
    return False


print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee']))
