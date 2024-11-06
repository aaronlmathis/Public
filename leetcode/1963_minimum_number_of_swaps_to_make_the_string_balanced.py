"""
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.
A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
Example 2:
(imbalance + 1) / 2;
Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".
Example 3:

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
 
"""

class Solution:
    def minSwaps(self, s: str) -> int:
        """
        if s == '[]':
            return 0
        
        def is_balanced(s) -> bool:
            o, c = 0,0
            for ch in s:
                if ch == '[':
                    o+=1
                elif ch == ']':
                    c+=1
                if c > o:
                    return False
            return True
        
        def last_opening(s) -> int:
            for x in range(len(s)-1, -1, -1):
                if s[x] == '[':
                    return x
        
        def first_imbalance(s):
            o, c = 0,0
            for x in range(len(s)):
                if s[x] == '[':
                    o+=1
                elif s[x] == ']':
                    c+=1
                if c > o:
                    return x

        count=0
        s = [char for char in s]
        while not is_balanced(s):
            tmp = s[first_imbalance(s)]
            s[first_imbalance(s)] = s[last_opening(s)]
            s[last_opening(s)] = tmp
            count+=1

        return count
        """
        count = 0
        for ch in s:
            if ch=='[':
                count+=1
            elif ch==']':
                if count > 0:
                    count-=1
        return (count+1) // 2



    
sol = Solution()
s = "][]["
print(sol.minSwaps(s))