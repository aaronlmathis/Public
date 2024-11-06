class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Lengths of haystack and needle
        haystack_len = len(haystack)
        print(f"Haystack_len: {haystack_len}")
        needle_len = len(needle)
        print(f"Needle_len: {needle_len}")
        
        # If needle is empty, return 0 (as per convention)
        if needle_len == 0:
            return 0
        
        # Loop through the haystack
        for i in range(haystack_len - needle_len + 1):
            # Check if the substring of haystack matches needle
            print(i)
            if haystack[i:i + needle_len] == needle:
                return i
        
        # If needle is not found, return -1
        return -1

haystack = "sadbutsad"
needle = "sad"     

sol = Solution()
val = sol.strStr(haystack, needle)
print(val)