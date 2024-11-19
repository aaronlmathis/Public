"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
"""
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq_seen = set()
        seq_repeated = set()

        for i in range(len(s) - 9):
            slice = s[i:i+10]
            if slice not in seq_seen:
                seq_seen.add(slice)
            else:
                seq_repeated.add(slice)
        return list(seq_repeated)


sol = Solution()
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" #Output: ["AAAAACCCCC","CCCCCAAAAA"]
print(sol.findRepeatedDnaSequences(s))