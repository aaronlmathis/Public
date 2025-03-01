"""
Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.
 

Example 1:
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16
 
Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100

"""
from typing import List
from itertools import combinations
def get_all_subarrays(input_list):
    """
    Generates all subarrays of a list using itertools.combinations.

    Args:
        input_list: The list for which to generate subarrays.

    Returns:
        A list of all subarrays of the input list.
    """
    subarrays = []
    for start in range(len(input_list)):
        for end in range(start + 1, len(input_list) + 1):
            subarrays.append(input_list[start:end])
    return subarrays

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # initialize odd/even count, curr_sum, and answer
        odd, even, curr_sum, answer = 0, 1, 0, 0
        MOD = 10**9 + 7

        # Iterate through `arr`, adding `num` to `curr_sum`.
        # If `curr_sum` is odd, add the `even` count to the `answer`
        # If `curr_sum` is even, add the `odd` count to the `answer`
        for num in arr:
            curr_sum += num
            if curr_sum & 1:
                answer += even
                odd+=1
            else:
                answer += odd
                even+=1
            
            answer % MOD

        return answer
sol = Solution()
arr = [1,2,3,4,5,6,7]
arr = [1,3,5]
#arr = [4,9,5,7,3,8,1]
print(sol.numOfSubarrays(arr))        