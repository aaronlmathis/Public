"""
Given an integer n, find a sequence that satisfies all of the following:

    - The integer 1 occurs once in the sequence.
    - Each integer between 2 and n occurs twice in the sequence.
    - For every integer i between 2 and n, the distance between the two occurrences of i is exactly i.

The distance between two numbers on the sequence, a[i] and a[j], is the absolute difference of their indices, |j - i|.

Return the lexicographically largest sequence. It is guaranteed that under the given constraints, there is always a solution.

A sequence a is lexicographically larger than a sequence b (of the same length) if in the first position where a and b differ, sequence a has a number greater than the corresponding number in b. For example, [0,1,9,0] is lexicographically larger than [0,1,5,6] because the first position they differ is at the third number, and 9 is greater than 5.

Example 1:
Input: n = 3
Output: [3,1,2,3,2]
Explanation: [2,3,2,1,3] is also a valid sequence, but [3,1,2,3,2] is the lexicographically largest valid sequence.

Example 2:
Input: n = 5
Output: [5,3,1,4,3,5,2,4,2]
"""
import time

def timed(function):
    def wrapper(*args, **kwargs):
        before = time.perf_counter()  # High-precision timing
        value = function(*args, **kwargs)
        after = time.perf_counter()
        fname = function.__name__
        print(f"{fname} took {after - before:.8f} seconds to execute!")  # Format for better precision
        return value
    return wrapper
from typing import List
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = 2 * n - 1
        result = [0] * size  
        used = [False] * (n + 1)  
        found = False  

        def backtrack(index: int):
            nonlocal found
            if found:
                return True 
            
            # Skip filled positions
            while index < size and result[index] != 0:
                index += 1
            if index >= size:
                found = True
                return True  # Solution found
            
            # Try placing numbers from `n` to `1`
            for num in range(n, 0, -1):
                if used[num]:  # Skip if number is already used
                    continue

                if num == 1:  # Number `1` only occupies one slot
                    result[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    result[index] = 0
                    used[1] = False
                else:
                    if index + num >= size or result[index + num] != 0:
                        continue  # Skip invalid placements

                    # Place `num`
                    result[index] = result[index + num] = num
                    used[num] = True

                    if backtrack(index + 1):
                        return True

                    # Undo placement (backtracking)
                    result[index] = result[index + num] = 0
                    used[num] = False

            return False  # No valid placement found

        backtrack(0)
        return result

sol = Solution()
pattern = []
for n in range(1,50):
    pattern.append(sol.constructDistancedSequence(n))
for pat in pattern:
    print(pat)
"""
        
        numbers = [x for x in range(n, 0, -1)] * 2
        numbers.pop()
        num_count = Counter(numbers)
        num_count[n] -=1

        #print(numbers)
        #print(num_count)
        #print()
        result = []
        def backtrack(choices, state, last_index):
            if len(state) == len(numbers):
                result.append(state[:])
            
            for k, v in choices.items():
                #print(choices)
                if v > 0 and (last_index[k] == -1 or abs(len(state) - last_index[k]) == k):
                    #print()
                    #print(last_index)
                    #print(f"k: {k} li: {last_index[k]} ci: {len(state)} - abs {abs((len(state)) - last_index[k])}")
                    state.append(k)
                    choices[k] -= 1
                    li = last_index[k]
                    last_index[k] = len(state)-1
                    #print(state)
                    #print(last_index)
                    #print()
                    backtrack(choices, state, last_index)

                    state.pop()
                    choices[k]+=1
                    last_index[k] = li
        
        last_index = [-1] * (n+1)
        last_index[n] = 0
        #print(last_index)
        #print()
        backtrack(num_count, [n], last_index)
        
        return result[0]
"""