def all_construct(target, char_list, memo={}):
    if target == '':
        return [[]]

    if target in memo:
        return memo[target]

    possible_list = []

    for char in [x for x in char_list if len(x) <= len(target)]:
        if target.startswith(char):
            pre_container = all_construct(target[len(char):], char_list, memo)
            if pre_container is not None:
                pre_list = [x + [char] for x in pre_container]
                possible_list = possible_list + pre_list

    memo[target] = possible_list
    return possible_list


print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
print(all_construct('zzz', ['z', 'zz', 'zzz']))
# print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']))
