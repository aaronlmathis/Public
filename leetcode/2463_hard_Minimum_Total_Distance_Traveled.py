"""
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.

"""
from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        
        # Sort the factories and robots
        robot.sort()
        factory.sort()

        # Unpack factories, If a factory can repair 2 robots, create two list items with its position in the list.
        factories = [f[0] for f in factory for _ in range(f[1])]
        
        n = len(robot)
        m = len(factories)
        
        # Initialize DP Table where dp[i][j] = Let dp[i][j] represent the minimum distance for the first i robots visiting the first j factories.
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):
            dp[0][j] = 0  # base case: no robots need no distance

        # Fill DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(robot[i-1] - factories[j-1]))

        #Return distance for all robots / all factories.
        
        return dp[n][m]
       
    

sol = Solution()
robot = [0,4,6]
factory = [[2,2],[6,2]]        
print(sol.minimumTotalDistance(robot, factory))