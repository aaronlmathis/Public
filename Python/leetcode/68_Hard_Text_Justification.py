"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
 
"""
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        output = []  # The text output once justified.
        #counts = {k: len(v) for k, v in enumerate(words)}  # Dictionary where key = idx of words and value equals length of word.
        counts = [len(v) for v in words]
        idx = 0
        n = len(words)
        
        while idx < n:
            line = []
            lineLength, numWords, numGaps, spacePerGap, diff = 0, 0, 0, 0, 0
            endLine = False

            # Build the current line up to the maxWidth
            while idx < n and lineLength + counts[idx] + numWords <= maxWidth:
                lineLength += counts[idx]
                line.append(words[idx])
                idx += 1
                numWords += 1
                if idx == n:
                    endLine = True

            # Calculate remaining spaces to fill the line
            diff = maxWidth - lineLength
            numGaps = numWords - 1 if numWords > 1 else 1

            if endLine:
                # For the last line, left-align with single spaces between words and remaining spaces at the end
                if numWords == 1:
                    # Only one word: add all remaining spaces to the end
                    justifiedLine = line[0] + ' ' * diff
                else:
                    # Multiple words: single space between words, remaining spaces at the end
                    justifiedLine = ' '.join(line) + ' ' * (diff - (numWords - 1))
            else:
                # For justified lines
                spacePerGap = diff // numGaps
                extraSpaces = diff % numGaps

                # Build gaps with even distribution, starting extra spaces from the left
                gaps = [' ' * (spacePerGap + 1) if i < extraSpaces else ' ' * spacePerGap for i in range(numGaps)]
                
                # Insert gaps between words
                justifiedLine = ''.join(word + gaps[i] if i < len(gaps) else word for i, word in enumerate(line))

            # Add the justified line to the output
            output.append(justifiedLine)

        return output

words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
sol = Solution()
print(sol.fullJustify(words, maxWidth))
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(sol.fullJustify(words, maxWidth))
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(sol.fullJustify(words, maxWidth))