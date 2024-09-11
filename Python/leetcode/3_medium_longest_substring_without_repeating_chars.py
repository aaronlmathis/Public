class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        n = len(s)
        max_length = 0
        
        for i in range(n):
            seen = set()
            current_substring = ""
            
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                current_substring += s[j]
                substrings.append(current_substring)
                if len(current_substring) > max_length:
                    max_length = len(current_substring)
        
        return max_length 
    
sol = Solution()
s = "pwwkew"
print(sol.lengthOfLongestSubstring(s))