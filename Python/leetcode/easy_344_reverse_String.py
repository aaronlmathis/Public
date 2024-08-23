class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        res = []

        for item in s[::-1]:
            res.append(item)

        for i in range(len(s)):
            s[i] = res[i]


        

sol = Solution()
s = ["h","e","l","l","o"]
print(sol.reverseString(s))