
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

""" 
Dynamic Programming
___________________

1. Recursion
2. Memoization
3. Bottom up (tabulation)

"""
n = 20

# 1 Recursion
@timed
def fib_1(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_1(n-1) + fib_1(n-2)
    return result

#print(f"Recursion: {fib_1(n)}")

# 2 Memoization
@timed
def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n] = result
    return result

memo = [None] * (n+1)
#print(f"Memoization: {fib_2(n, memo)}")

# 3 Bottom-Up
@timed
def fib_3(n):
    if n == 1 or n == 2:
        return 1
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 1
    
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

n = 10
dp = fib_3(n)
print(dp)
