"""
You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

 

Example 1:

Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"
Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
Example 2:

Input: s = "aababab", repeatLimit = 2
Output: "bbabaa"
Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa". 
The letter 'a' appears at most 2 times in a row.
The letter 'b' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
 
"""
import heapq
from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count the frequency of each character in the string 's'
        chars = Counter(s)

        # Sort the characters by frequency in descending order
        # 'sorted_chars' will be a list of tuples: (char, frequency)
        sorted_chars = sorted(chars.items(), reverse=True)

        # Initialize the result list to build the final answer
        ans = []

        # Process characters while there are still characters to handle
        while sorted_chars:
            # Take the character with the highest frequency
            char, freq = sorted_chars[0]
            
            # If the frequency is within the repeat limit, append all occurrences
            if freq <= repeatLimit:
                ans.append(char * freq)  # Append 'char' repeated 'freq' times
                sorted_chars.pop(0)      # Remove the character from the list
            else:
                # If the frequency exceeds the repeat limit, append only 'repeatLimit' times
                ans.append(char * repeatLimit)
                # Update the remaining frequency of the character
                sorted_chars[0] = (char, freq - repeatLimit)
                
                # If there's another character available, insert it to break the repetition
                if len(sorted_chars) > 1:
                    next_char, next_freq = sorted_chars[1]
                    ans.append(next_char)  # Append one occurrence of the next character
                    
                    # Update or remove the next character based on its remaining frequency
                    if next_freq == 1:
                        sorted_chars.pop(1)  # Remove the character if fully used
                    else:
                        sorted_chars[1] = (next_char, next_freq - 1)  # Decrement its frequency
                else:
                    # If no other characters are available, break the loop
                    break

        # Join the list of characters into a final string and return it
        return ''.join(ans)


sol = Solution()
s = "cczazcc"
repeatLimit = 3     
print(sol.repeatLimitedString(s, repeatLimit))   
s = "aababab"
repeatLimit = 2
print(sol.repeatLimitedString(s, repeatLimit))  