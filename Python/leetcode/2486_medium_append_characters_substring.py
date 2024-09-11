class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        
        # Iterate over s to check how much of t is a subsequence in s
        for char in s:
            if i < len(t) and char == t[i]:
                i += 1
        
        # The number of characters remaining in t that need to be appended
        return len(t) - i



s = "vrykt"
t = "rkge"

sol = Solution()
print(sol.appendCharacters(s, t))
