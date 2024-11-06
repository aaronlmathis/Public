"""
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.


Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
"""
import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []

        #Create Max Heap of Letters
        max_heap = []
        if a > 0:
            heapq.heappush(max_heap, (-a, 'a'))
        if b > 0: 
            heapq.heappush(max_heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(max_heap, (-c, 'c'))


        while max_heap:  # Loop while max_heap has items
            print(max_heap)

            count1, letter1 = heapq.heappop(max_heap) # Pop the max item
            if len(ans) > 1 and ans[-1] == letter1 and ans[-2] == letter1: #Check to see if the letter popped is the last two letters in the list (if the list is at least 2 letters)
                if not max_heap:    # Check if there are other letters and if not, break loop
                    break
                count2, letter2 = heapq.heappop(max_heap) # Pull next greatest letter from max heap
                ans.append(letter2) # Add letter to answer
                if count2 + 1 < 0: #Push letter back into max_heap if it isn't zero.
                    heapq.heappush(max_heap, (count2 + 1, letter2))
                heapq.heappush(max_heap, (count1, letter1)) #Push original letter back into max_heap to be used again
            else:
                ans.append(letter1) #add letter to answer
                if count1 + 1 < 0: #add letter back to max_heap unless it is zero.
                    heapq.heappush(max_heap, (count1 + 1, letter1))

        return ''.join(ans) #return string answer



a = 1
b = 1
c = 7
sol = Solution()
print(sol.longestDiverseString(a,b,c))        