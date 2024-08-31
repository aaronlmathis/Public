class Solution:
    def makeGood(self, s: str) -> str:
        done = False
        while not done:
            done = True  # Assume we're done unless we find a pair to remove
            for i in range(len(s) - 1):
                if s[i].swapcase() == s[i + 1]:
                    s = s[:i] + s[i + 2:]  # Remove the adjacent pair
                    done = False  # Set done to False because we made a change
                    break  # Exit the loop to restart from the beginning
        return s



sol = Solution()
s = "leEeetcodeE"
print(sol.makeGood(s))