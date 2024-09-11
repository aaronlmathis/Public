class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        w = s.split()
        l = len(w[-1])
        return l


sol = Solution()
print(sol.lengthOfLastWord("This is a Test"))