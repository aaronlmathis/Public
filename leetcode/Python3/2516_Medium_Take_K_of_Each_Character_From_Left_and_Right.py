"""
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

Example 1:
Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.

Example 2:
Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
"""
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # Total counts
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1

        # Quick exit
        if min(count) < k:
            return -1

        # Sliding Window
        minutes = float("inf")
        left = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord('a')] -= 1

            while min(count) < k:
                count[ord(s[left]) - ord('a')] += 1
                left += 1
            minutes = min(minutes, len(s) - (right - left + 1))
        return minutes
        
 
s = "aabaaaacaabc"
k = 2
sol = Solution()
print(sol.takeCharacters(s, k))        
"""
       left = -1
        count = {}
        minMinutes = float('inf')
        while left < n-1:
            count.clear()
            minutes = 0
            for l in range(0, left+1):
                count[s[l]] = count.get(s[l], 0) + 1
                minutes+=1

            right = n-1
            while right >= left + 1:
                if count.get('a', 0) >= k and count.get('b', 0) >= k and count.get('c', 0) >= k:
                    break 
                count[s[right]] = count.get(s[right], 0) + 1
                minutes+=1
                right-=1
            minMinutes = min(minMinutes, minutes)
            left+=1

        return minMinutes

"""