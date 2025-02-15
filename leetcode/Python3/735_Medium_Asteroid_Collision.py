"""
We are given an array asteroids of integers representing asteroids in a row. The indices of the asteriod in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 

Constraints:

2 <= asteroids.length <= 104
-1000 <= asteroids[i] <= 1000
asteroids[i] != 0
"""
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 1:
            return asteroids
        stack = []
        for asteroid in asteroids:
            if stack and stack[-1] > 0 and asteroid < 0:
                while len(stack) > 0 and stack[-1] > 0 and asteroid < 0:
                    if stack[-1] == abs(asteroid):
                        stack.pop()
                        asteroid = 0
                    elif stack[-1] > abs(asteroid):
                        asteroid = 0
                    else: 
                        stack.pop()
                if asteroid:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack

sol = Solution()      
asteroids = [5,10,-5]  
print(f"{sol.asteroidCollision(asteroids)}\tExpected: [5, 10]")
asteroids = [8,-8]
print(f"{sol.asteroidCollision(asteroids)}\tExpected: []")
asteroids = [10,2,-5] 
print(f"{sol.asteroidCollision(asteroids)}\tExpected: [10]")
asteroids =[-2,-1,1,2]
print(f"{sol.asteroidCollision(asteroids)}\tExpected: [-2, -1, 1, 2]")
asteroids =[1,-2,-2,-2]
print(f"{sol.asteroidCollision(asteroids)}\tExpected: [-2, -1, 1, 2]")