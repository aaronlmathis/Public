"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1

Constraints:
1 <= n <= 9
"""
class Solution:
    def totalNQueens(self, n: int) -> int:
        used_cols = set()
        used_diagonals1 = set()  # Tracks row - col
        used_diagonals2 = set()  # Tracks row + col
        solutions = set()
        answer = 0

        def backtrack(row, placed):
            nonlocal answer
            if row == n:  # Base case: All n queens are placed
                f_placed = frozenset(placed)
                if f_placed not in solutions:
                    solutions.add(f_placed)
                    answer += 1
                return

            for col in range(n):
                if col in used_cols or (row - col) in used_diagonals1 or (row + col) in used_diagonals2:
                    continue  # Skip invalid placements

                # Place queen
                used_cols.add(col)
                used_diagonals1.add(row - col)
                used_diagonals2.add(row + col)
                placed.add((row, col))

                backtrack(row + 1, placed)

                # Remove queen (backtrack)
                used_cols.remove(col)
                used_diagonals1.remove(row - col)
                used_diagonals2.remove(row + col)
                placed.remove((row, col))

        backtrack(0, set())  # Start with row 0
        return answer


sol = Solution()
n = 4
print(sol.totalNQueens(n))