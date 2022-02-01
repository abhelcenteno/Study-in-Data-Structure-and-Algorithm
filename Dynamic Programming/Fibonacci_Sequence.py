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

def fib3(num):
    table = [0, 1]
    if num in table:
        return table[num]

    for n in range(2,num+1):
        table.append(table[n-2] + table[n-1])

    return table[num]

def fib4(num):
    a = 0
    b = 1

    for n in range(num):
        a, b = b, a+b

    return a


print(fib1(10))
print(fib2(1000))
print(fib3(1000))
print(fib4(100000))
