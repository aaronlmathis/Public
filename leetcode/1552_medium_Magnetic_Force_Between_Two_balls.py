"""
In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
Example 2:
"""
from typing import List
class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]

        def place_ball(min_distance):
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= min_distance:
                    count+=1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        while left <= right:
            mid = (left + right) // 2
            if place_ball(mid):
                left = mid + 1
            else:
                right = mid -1

        return right

        print(abs(position[right] - position[left]))
sol = Solution()
position = [1,2,3,4,7]
m = 3
print(sol.maxDistance(position,m))