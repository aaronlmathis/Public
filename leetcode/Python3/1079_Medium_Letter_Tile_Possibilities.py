"""
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

Example 2:
Input: tiles = "AAABBC"
Output: 188

Example 3:
Input: tiles = "V"
Output: 1

Constraints:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.
"""
from itertools import permutations, combinations
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
from collections import Counter
from math import factorial
class Solution:
    @staticmethod
    def get_possible(tiles) -> set:
        unique_results = set()
        for i in range(1, len(tiles) + 1):
            for combo in combinations(tiles, i):  # Select different lengths
                for perm in permutations(combo):  # Get all orderings of that subset
                    unique_results.add("".join(perm))
        return unique_results
    
    @timed
    def numTilePossibilities(self, tiles: str) -> int:
        remaining = list(Counter(tiles).values())
        ans = 0
        res = [0] * len(remaining)

        def backtrack(i):
            nonlocal ans
            permutations = 1
            for x in res:
                if x > 0:
                    permutations *= factorial(x)
            ans += factorial(sum(res)) // permutations

            for j in range(i, len(remaining)):
                if remaining[j] > 0:
                    res[j] += 1
                    remaining[j] -= 1
                    backtrack(j)
                    res[j] -= 1
                    remaining[j] += 1

        backtrack(0)
        return ans



sol = Solution()
tiles = "AAB"
print(f"{sol.numTilePossibilities(tiles)} - 8")
tiles = "AAABBC"
#print(f"{sol.numTilePossibilities(tiles)} - 188")
tiles = "V"
#print(f"{sol.numTilePossibilities(tiles)} - 1")
