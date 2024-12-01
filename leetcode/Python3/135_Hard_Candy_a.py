"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        children = [1] * n

        for i in range(0, n-1):
            print(f"{ratings[i]} - {ratings[i+1]}")
            if ratings[i+1] > ratings[i] and children[i+1] <= children[i]:
                children[i+1] = children[i] + 1
        print(children)
        
        for i in range(n-1, 0, -1):
            print(f"{ratings[i]} - {ratings[i-1]}")
            if ratings[i-1] > ratings[i] and children[i-1] <= children[i]:
                children[i-1] = children[i] + 1
        print(children)
        return sum(candy for candy in children)




ratings = [1,0,2]
sol = Solution()
print(sol.candy(ratings))
