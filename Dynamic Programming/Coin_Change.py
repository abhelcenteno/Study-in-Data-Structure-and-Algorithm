def coin_change1(coin_list, change, memo={}):
    # in-depth recursion from top to bottom to top with the help of memoization
    min_coins = change
    if change in coin_list:
        memo[change] = 1
        return 1
    elif change in memo:
        return memo[change]
    else:
        for coin in [x for x in coin_list if x <= change]:
            num_coins = 1 + coin_change1(coin_list, change - coin, memo)
            if num_coins < min_coins:
                min_coins = num_coins
            memo[change] = min_coins

    return min_coins


def coin_change2(coin_list, change):  # from bottom to top
    change_container = [change + 1] * (change + 1)
    change_container[0] = 0
    for num in range(1, change + 1):
        for possible in [x for x in coin_list if x <= num]:
            change_container[num] = min(change_container[num], 1 + change_container[num - possible])

    return change_container[change] if change_container[change] != change + 1 else -1


# plan soon is to make coin_change that outputs which coins or denomination is to be used

print(coin_change1([1, 5, 10, 25], 100))
print(coin_change2([20, 50, 100, 200, 500, 1000], 200000))
