class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        lst = [c for c in columnTitle]
        num = 0
        for v in lst:
            num = num * 26 + (ord(v) - ord('A') + 1)
        return num