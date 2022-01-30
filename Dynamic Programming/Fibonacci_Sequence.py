def fib1(n):  # not optimized
    if n <= 1:
        return n
    else:
        return fib1(n-1) + fib1(n-2)


def fib2(n, memo={}):  # optimized using memoization
    if n <= 1:
        memo[n] = n
        return memo[n]
    elif n in memo:
        return memo[n]
    else:

        ans = fib2(n-2, memo) + fib2(n-1, memo)
        memo[n] = ans
        return memo[n]


print(fib1(10))
print(fib2(10))
