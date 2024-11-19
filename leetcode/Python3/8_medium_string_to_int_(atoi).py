class Solution:
    def myAtoi(self, s: str) -> int:
        pos = True
        start = 0
        s = s.strip()
        if s == '':
            return 0

        if s[0] == '+':
            pos = True
            start = 1
        elif s[0] == '-':
            pos = False
            start = 1
        elif s[0].isalpha():
            return 0
        new =''
        index = start
        while index < len(s):
            if s[index].isnumeric():
                new += s[index]
            if not s[index].isnumeric():
                break
            index+=1
        if new == '':
            return 0

        res = int(new) if pos else int(new) * -1 
        if res > 2 ** 31 -1 : 
            res = 2147483647
        if res < -2 ** 31:
            res = -2147483648
    
        return res

sol = Solution()
print(sol.myAtoi('   -042'))