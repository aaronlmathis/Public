class Solution:
    def sortJumbled(self, mapping: list[int], nums: list[int]) -> list[int]:
        #Step 1: find all the mapped values and add to dictionary. k: num v:mapped value
        mapped_values = {}
        for num in nums: # loop through items in nums list
            mapped_values[num] = '' #add the number to the dictionary as a blank string
            for n in str(num): #loop through characters
                mapped_values[num] += str(mapping[int(n)])

        for k, v in mapped_values.items():
            mapped_values[k] = int(v)

        mapped_sorted = sorted(mapped_values.items(), key=lambda x: x[1])

        res = []
        for k, v in mapped_sorted:
            res.append(k)

        return res


mapping = [8,9,4,0,2,1,3,5,7,6]
nums = [991,338,38]

sol = Solution()
print(sol.sortJumbled(mapping, nums))


"""
You are given a 0-indexed integer array mapping which represents the mapping rule of a shuffled decimal system. mapping[i] = j means digit i should be mapped to digit j in this system.

The mapped value of an integer is the new integer obtained by replacing each occurrence of digit i in the integer with mapping[i] for all 0 <= i <= 9.

You are also given another integer array nums. Return the array nums sorted in non-decreasing order based on the mapped values of its elements.

Notes:

Elements with the same mapped values should appear in the same relative order as in the input.
The elements of nums should only be sorted based on their mapped values and not be replaced by them.
"""