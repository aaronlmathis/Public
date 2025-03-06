"""
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
"""
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        k2 = k * 2
        s_array = []
        for i in range(0, n-k, k):
            print(s[i:i+k])
            s_array.append(s[i:i+k])
        s_array.append(s[i+k:])
        print(s_array)
        for i in range(0, len(s_array), 2):
            s_array[i] = s_array[i][::-1]
        return ''.join(s_array)

sol = Solution()
s = "abcdefg"
k = 2
print(sol.reverseStr(s, k))        
        