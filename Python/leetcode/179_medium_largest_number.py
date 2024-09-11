class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        new = [str(num) for num in nums]
        res = ''
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x+y < y+x:
                return 1
            else:
                return 0
        from functools import cmp_to_key
        new.sort(key=cmp_to_key(compare))
        res = ''.join(new)

        if res[0] == '0':
            return '0'
        else:      
            return res
    
sol= Solution()
nums = [3,30,34,5,9]
print(sol.largestNumber(nums))

"""
        # Convert all numbers to strings
        new = [str(num) for num in nums]

        # Custom sorting using lambda as the key function
        new.sort(key=lambda x: x*10, reverse=True)

        # Join the sorted numbers into a single string
        res = ''.join(new)

        # Edge case: when the largest number is 0 (e.g., [0, 0])
        if res[0] == '0':
            return '0'
        else:
            return res
"""

