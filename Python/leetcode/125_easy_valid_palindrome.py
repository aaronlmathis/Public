class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return cleaned == cleaned[::-1]    
    
    def isPalindrome_alt(self, s: str) -> bool:
        a = []
        for c in s:
            if c.isalnum():
                a.append(c.lower())
        na = [c for c in a]
        na.reverse()
        if na == a:
            return True
        return False
        
sol = Solution()
print(sol.isPalindrome("foop"))