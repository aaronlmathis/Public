"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:

1 <= m, n <= 100
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"function_name took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

class Solution:
    @timed
    def uniquePaths(self, m: int, n: int) -> int:

        dp  = [[0] * n for _ in range(m) ]

        """ Tabulation """
        dp[0][0] = 1

        for j in range(1, n):
            dp[0][j] = dp[0][j-1]


        for i in range(1, m):
            dp[i][0] = dp[i-1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        paths = dp[m-1][n-1]
        """ MEMOIZATION 
        def find_paths(row, col):
            if (row, col) == (m-1, n-1):
                return 1

            if dp[row][col] != -1:
                return dp[row][col]

            right = down = 0
            
            # Go Down
            if row + 1 < m:
                down = find_paths(row+1, col)

            # Go Right
            if col+1 < n:
                right = find_paths(row, col+1)
            
            dp[row][col] = right+down

            return right + down
        
        paths = find_paths(0,0)
        """
        return paths

m = 3
n = 7
sol = Solution()
print(sol.uniquePaths(m, n))