"""
Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. 
However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
"""
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def backtrack(start, seen_substrings):
            if start >= len(s):
                return len(seen_substrings)

            # Memoization to track max_splits and avoid recomputation
            max_splits = 0  
            for i in range(start, len(s)):  # Explore all possible substrings starting from `start`
                substring = s[start:i + 1]  # `i + 1` to include the character at `i`
                if substring not in seen_substrings:  # Check if the substring is unique
                    seen_substrings.add(substring)  # Add it to the set
                    # Recurse and update the max_splits with the maximum from the recursive call
                    max_splits = max(max_splits, backtrack(i + 1, seen_substrings))
                    seen_substrings.remove(substring)  # Backtrack: undo the decision

            return max_splits  # Return the maximum number of unique substrings found

        return backtrack(0, set())  # Start the backtracking with an empty set

s = "ababccc"
sol = Solution()
print(sol.maxUniqueSplit(s))
        