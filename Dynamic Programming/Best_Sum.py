def best_sum(target, num_list, memo={}):
    if target == 0:
        return []

    if target in memo:
        return memo[target]

    shortest_combination = None
    for num in [x for x in num_list if x <= target]:
        remainder = target - num
        result = best_sum(remainder, num_list, memo)
        if result is not None:
            result = result + [num]
            if shortest_combination is None or len(shortest_combination) > len(result):
                shortest_combination = result.copy()

    memo[target] = shortest_combination
    return shortest_combination


print(best_sum(7, [5, 3, 4, 7]))
print(best_sum(8, [2, 3, 5]))
print(best_sum(8, [1, 4, 5]))
print(best_sum(100, [1, 2, 5, 25]))
