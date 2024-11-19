"""
You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

A store can only be given at most one product type but can be given any amount of it.
After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
Return the minimum possible x.

Example 1:
Input: n = 6, quantities = [11,6]
Output: 3
Explanation: One optimal way is:
- The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
- The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.

Example 2:
Input: n = 7, quantities = [15,10,10]
Output: 5
Explanation: One optimal way is:
- The 15 products of type 0 are distributed to the first three stores in these amounts: 5, 5, 5
- The 10 products of type 1 are distributed to the next two stores in these amounts: 5, 5
- The 10 products of type 2 are distributed to the last two stores in these amounts: 5, 5
The maximum number of products given to any store is max(5, 5, 5, 5, 5, 5, 5) = 5.

Example 3:
Input: n = 1, quantities = [100000]
Output: 100000
Explanation: The only optimal way is:
- The 100000 products of type 0 are distributed to the only store.
The maximum number of products given to any store is max(100000) = 100000.
Binaray search with left = average number in quantities and right = max number among quantities
mid = (left + right) / 2
each mid write a function to check weather it is able to divide to n stores return res <= n
if possible then add r = mid to narrow down the search
if not then l = mid + 1 to expand more.
"""
from typing import List
from math import ceil

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        
        # Helper function `canDistribute` checks if it’s possible to distribute products
        # with a given maximum number of products per store (`maxProducts`).
        def canDistribute(maxProducts: int) -> bool:
            requiredStores = 0
            for quantity in quantities:
                # Calculate the number of stores required for the current quantity
                # by dividing quantity by maxProducts and rounding up.
                # `ceil` ensures each store gets the correct number of products
                # without exceeding `maxProducts`.
                requiredStores += ceil(quantity / maxProducts)
            
            # Return true if required stores are less than or equal to the available `n`.
            return requiredStores <= n

        # Set initial search bounds for binary search.
        left, right = 1, max(quantities)  # Left bound is 1, right bound is the max in `quantities`.
        result = 0

        # Perform binary search to find the minimum possible `maxProducts` value.
        while left <= right:
            mid = left + (right - left) // 2  # Calculate the middle value to test.
            
            # Use `canDistribute` to check if `mid` products per store is feasible.
            if canDistribute(mid):
                result = mid  # If feasible, `mid` is a candidate result.
                right = mid - 1  # Reduce the right bound to search for potentially smaller values.
            else:
                left = mid + 1  # If not feasible, increase the left bound to search larger values.
        
        # Return the smallest feasible maximum number of products per store.
        return result



sol = Solution()
n = 6
quantities = [11,6]
print(sol.minimizedMaximum(n, quantities))        