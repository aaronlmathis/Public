"""
A happy string is a string that:

    - consists only of letters of the set ['a', 'b', 'c'].
    - s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.

Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 
Constraints:
1 <= n <= 10
1 <= k <= 100
"""
from math import ceil, floor
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # Possible letters of a happy string
        letters = ['a', 'b', 'c']

        # The number of possible happy strings as a function of `n`
        total_poss = 3 * (3-1)**(n-1)
        
        # Quick Exit if `k` is greater than `total_poss`
        if k > total_poss:
            return '' 
        
        # Initialize empty string
        happy_string = []
        
        # `nn` tracks the remaining length to process
        nn = n

        # Iterate while `happy_string` is smaller than `n`
        while len(happy_string) < n:
            # `gr` is the number of substrings of `p` that start with either `a`, `b`, or `c`
            gr = total_poss // 3
            # `lg` or letter group is the group that the first letter of this substring starts with. (1=a, b=2, c=3)
            lg = ceil(k / gr)
            # First letter is equal to `lg-1` (since `letters` is a zero-indexed array)
            fl = letters[lg-1]
            # Add `fl` to happy string.
            happy_string.append(fl)
            # Decrease the number of remaining characters
            nn-=1
            # Recalculate `k`. We are no longer looking for the `k` substring of f(n) possible.
            # We are looking for `k - (lg-1) * g` of f(nn) possible.
            k -=(lg-1) * gr
            # Remove the selected letter from possible choices for the next iteration
            letters = [ch for ch in ['a', 'b', 'c'] if ch != fl]

            # Cut the total possible in half
            total_poss //= 2

        return ''.join(happy_string)
        
sol = Solution()

n = 3
k = 9

print(sol.getHappyString(n,k))
#Output      "ababcababc"
#Expected    "abacbabacb"