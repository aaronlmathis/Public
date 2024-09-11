memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    
    if n <= 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)

    memo[n] = result
    return result


def fib1(n):
    memo = {}
    for i in range(1, n+1):
        if i <= 2:
            result = 1
        else:
            result = memo[i-1] + memo [i-2]
        memo[i] = result
    return memo[n]

#print(fib1(50))

def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)


def min_coins(m, coins):
    if m in memo:
        return memo[m]
    if m == 0:
        answer = 0
    else:
        answer = None
        for coin in coins:
            subproblem = m - coin
            if subproblem < 0 :
                continue
            answer = min_ignore_none(answer, min_coins(subproblem, coins)+1)
    memo[m] = answer
    return answer

#print(min_coins(150, [1,4,5]))

def min_coins1(m, coins):
    memo = {}
    memo[0] = 0
    for i in range(1, m+1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(memo.get(i), memo.get(subproblem) + 1)
    return memo[m]

#print(min_coins1(150, [1,4,5]))
