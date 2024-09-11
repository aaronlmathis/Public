class Solution:
    def scoreOfString(self, s: str) -> int:
        ascii = [ord(c) for c in s]
        scores = []
        for i in range(len(ascii)-1):
            scores.append(abs(ascii[i] - ascii[i+1]))
        return sum(scores)

s = "hello"
sol = Solution()
print(sol.scoreOfString(s))