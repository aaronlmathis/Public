class Solution:
    def splitNum(self, num: int) -> int:

        s = str(num)
        
        # Step 2: Sort the characters in the string
        sorted_digits = sorted(s)
        
        # Step 3: Form two integers by picking digits alternately
        num1, num2 = '', ''
        
        for i in range(len(sorted_digits)):
            if i % 2 == 0:
                num1 += sorted_digits[i]
            else:
                num2 += sorted_digits[i]
        
        # Convert them back to integers
        num1 = int(num1)
        num2 = int(num2)
        
        # Step 4: Return the sum of the two integers
        return num1 + num2
                

num = 4325
sol = Solution()
print(sol.splitNum(num))        