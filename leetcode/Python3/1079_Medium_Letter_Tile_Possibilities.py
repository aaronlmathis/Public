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

class Solution:
    @staticmethod
    def get_possible(tiles) -> set:
        unique_results = set()
        for i in range(1, len(tiles) + 1):
            for combo in combinations(tiles, i):  # Select different lengths
                for perm in permutations(combo):  # Get all orderings of that subset
                    unique_results.add("".join(perm))
        return unique_results
    

    def numTilePossibilities(self, tiles: str) -> int:
        result = []
        def backtrack(letter_count, state):
            if state and state not in result:
                result.append(state[:])
            
            for k, v in letter_count.items():
                if v > 0:
                    state.append(k)
                    letter_count[k]-=1
                    backtrack(letter_count, state)
                
                    state.pop()
                    letter_count[k]+=1
        
        #print(f"Answer: {self.get_possible(tiles)}")
        letter_count = {}
        for c in tiles:
            letter_count[c] = letter_count.get(c, 0) + 1
        
        print(f"Letter Count: {letter_count}")
        backtrack(letter_count, [])
        
        return len(result)



sol = Solution()
tiles = "AAB"
print(f"{sol.numTilePossibilities(tiles)} - 8")
tiles = "AAABBC"
#print(f"{sol.numTilePossibilities(tiles)} - 188")
tiles = "V"
#print(f"{sol.numTilePossibilities(tiles)} - 1")
