class Solution:
    def reverse(self, x: int) -> int:
        bound = -2 ** 31
        bound2 = 2 ** 31 -1
        st = str(x)
        isNeg = True if st[0] == '-' else False
        
        if isNeg:
            st = st.replace('-', '')

        res = int(st[::-1]) if not isNeg else int(st[::-1]) * -1
        if res > 2147483647 or res < -2147483648:
            res = 0
            
        return res
    
sol = Solution()

print(sol.reverse(456325645879))