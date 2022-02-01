def count_construct(target, char_list, memo={}):
    if target == '':
        return 1

    if target in memo:
        return memo[target]

    counter = 0
    for char in [x for x in char_list if len(x) <= len(target)]:
        if target.startswith(char):
            pre_counter = count_construct(target[len(char):], char_list, memo)
            counter = counter + pre_counter

    memo[target] = counter
    return counter


print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                      ['e', 'ee', 'eee', 'eeee', 'eeeee']))
