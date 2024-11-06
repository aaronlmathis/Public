class Solution:
    def numSteps(self, s: str) -> int:
        dec = int(s, 2) #convert binary str to base2 integer.
        count=0
        while dec > 1: #Loop until number is 1.
            if dec % 2 == 0: #Number is even
                dec //= 2
            else: # Number is odd
                dec+=1
            count+=1
        return count
s = "1101"
sol = Solution()

print(sol.numSteps(s))