class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''
        for c in digits:
            s = s + str(c)

        s = int(s)
        s += 1

        s = str(s)
        out = []
        for c in s:
            out.append(int(c))

        return out