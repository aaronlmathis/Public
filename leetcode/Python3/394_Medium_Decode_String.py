"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: ""
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                p = stack.pop()
                tmp = ''
                while p != '[':
                    if len(p) > 1:
                        p = p[::-1]
                    tmp+=p
                    p = stack.pop()
                
                m = ''
                p = stack.pop()
                m+=p
                while stack and  stack[-1] in ['0','1','2','3','4','5','6','7','8','9']:
                    p = stack.pop()
                    m+=p
            
                stack.append(int(m[::-1]) * tmp[::-1] )
                print(f'adding: {int(m[::-1]) * tmp[::-1]} ')
                print(stack)
            else:
                stack.append(c)

        return ''.join(stack)
sol = Solution()
"""
s = "3[a]2[bc]"
print(f"{sol.decodeString(s)} -  aaabcbc")
s = "3[a2[c]]"
print(f"{sol.decodeString(s)} - accaccacc")
s = "2[abc]3[cd]ef"
print(f"{sol.decodeString(s)} - abcabccdcdcdef")    
s = "100[leetcode]"
print(sol.decodeString(s))
"""
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
print(f"{sol.decodeString(s)}\nzzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef")
s = "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"