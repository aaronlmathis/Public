"""
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

Constraints:

n == gain.length
1 <= n <= 100
-100 <= gain[i] <= 100
"""
from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        altitude, max_altitude = 0, 0
        for g in gain:
            altitude += g
            if altitude > max_altitude:
                max_altitude = altitude
        return max_altitude
        """
        # Set `n` to length of `gain`
        # Initialize `prefix_sums` array of size `n+1` populated with zeros.
        # Initialize `max_altitude` as equal to 0
        n = len(gain)
        prefix_sums = [0] * (n+1)


        # Iterate over `gain` list, calculating the new `altitude` as:
        # Previous Altitude + gain or `prefix_sums[i] + g`
        # Check if new `altitude` is greater than `max_altitude` seen.
        # If so, set `max_altitude` to `altitude`.
        for i, g in enumerate(gain):
            altitude = prefix_sums[i] + g
            prefix_sums[i+1] = altitude

        # Return max of prefix_sums

        return max(prefix_sums)  

sol = Solution()
gain = [-4,-3,-2,-1,4,3,2]
print(sol.largestAltitude(gain))

        