"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

 

Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
"""
from collections import deque
from typing import List
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
                
        visited = set()
        visited.add(startGene)
        
        bases = ['A', 'C', 'G', 'T']
        queue = deque([(0, startGene)])



        while queue:
            mutations, gene = queue.popleft()

            for i in range(len(gene)):
                # Try all possible mutations at position i
                for base in bases:
                    if gene[i] == base:
                        continue
                    mutated_gene = gene[:i] + base + gene[i+1:]
                    
                    # If the mutated gene is the end gene
                    if mutated_gene == endGene:
                        return mutations + 1
                    
                    # If the mutated gene is valid and not visited
                    if mutated_gene in bank and mutated_gene not in visited:
                        visited.add(mutated_gene)
                        queue.append((mutations + 1, mutated_gene))

        return -1

startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
sol = Solution()
print(sol.minMutation(startGene, endGene, bank))