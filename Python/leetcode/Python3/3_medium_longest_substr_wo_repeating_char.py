class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        max_length = 0
        left = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_length=max(max_length, right - left +1)
        
        return max_length

    
sol = Solution()
s = "abcabcbb"
print(sol.lengthOfLongestSubstring(s))