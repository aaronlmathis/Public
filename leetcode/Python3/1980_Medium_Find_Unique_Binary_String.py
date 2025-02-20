"""
Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper

from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Set `n` to be the length of one of the binary strings
        n = len(nums[0])

        # Initialize an empty string for the answer
        answer = ''

        # Initialize `found` as a boolean flag. This lets our function know when to stop backtracking.
        found = False

        # Helper backtracking function.
        def build_bstring(state: List[str]) -> None:
            # Bring `answer` and `found` into scope of the helper function.
            nonlocal answer, found

            # If the `found` flag is True, return from the current recursive call of this function.
            if found:
                return

            # If the current state of the list is the same size as `n`, we know we need to check if it is a possible string
            # by seeing if it is already in `nums`. If it isn't, set `answer` to it and set `found` to True. Then Return.
            if len(state) == n:
                # Join the `state` list into a string.
                possible_bstring = ''.join(state)
                # Check if string is not in nums already
                if possible_bstring not in nums:
                    answer = possible_bstring
                    found = True
                # Regardless of whether it is the answer, we still need to return because it cant be any longer
                return

            # This is the key logic of the backtracking function.
            # We make 2 choices here (since our option for the next number in the bstring is 0 or 1).
            # If we had more options, we might put a for loop and loop through all the options....

            # For each option (or iteration) we:
            #   1. Choose that option (append it to the state list)
            #   2. Call the backtrack function recursively, passing the new state
            #   3. Undo the option (pop it from state)
            # That way, we can move on to the next option and do the same, creating several paths to finding the answer.
            state.append('0')
            build_bstring(state)
            state.pop()

            state.append('1')
            build_bstring(state)
            state.pop()

        # Call the first call of the backtrack function, passing an empty list.
        build_bstring([])

        return answer




nums = ["111","011","001"]
sol = Solution()
print(sol.findDifferentBinaryString(nums))