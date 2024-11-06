class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        """
        s = [str(d) for d in digits]
        st=''.join(s)
        num = int(st) + 1
        s = []
        for n in str(num):
            s.append(n)
        return s
        """
        n = len(digits)
        
        # Traverse the list from the last digit to the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0
            digits[i] = 0
        
        # If all digits were 9, we need to add a leading 1
        return [1] + digits

sol=Solution()
digits = [9]
print(sol.plusOne(digits))