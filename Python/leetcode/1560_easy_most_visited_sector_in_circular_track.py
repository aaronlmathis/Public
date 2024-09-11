"""
Given an integer n and an integer array rounds. We have a circular track which consists of n sectors labeled from 1 to n. 
A marathon will be held on this track, the marathon consists of m rounds. The ith round starts at sector rounds[i - 1] and ends at sector rounds[i]. 
For example, round 1 starts at sector rounds[0] and ends at sector rounds[1]

Return an array of the most visited sectors sorted in ascending order.

Notice that you circulate the track in ascending order of sector numbers in the counter-clockwise direction (See the first example).
Input: n = 4, rounds = [1,3,1,2]
Output: [1,2]
Explanation: The marathon starts at sector 1. The order of the visited sectors is as follows:
1 --> 2 --> 3 (end of round 1) --> 4 --> 1 (end of round 2) --> 2 (end of round 3 and the marathon)
We can see that both sectors 1 and 2 are visited twice and they are the most visited sectors. Sectors 3 and 4 are visited only once.

"""
from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visit_count = [0] * (n + 1)  # Initialize visit count for each sector (1-indexed)

        # Mark all the sectors visited from rounds[i-1] to rounds[i]
        for i in range(1, len(rounds)):
            start = rounds[i - 1]
            end = rounds[i]
            # When start <= end, just go from start to end
            if start <= end:
                for j in range(start, end + 1):
                    visit_count[j] += 1
            # When start > end, go from start to n and then from 1 to end
            else:
                for j in range(start, n + 1):
                    visit_count[j] += 1
                for j in range(1, end + 1):
                    visit_count[j] += 1

        # Also count the last sector (rounds[-1])
        visit_count[rounds[-1]] += 1

        # Find the max visit count
        max_visit = max(visit_count)

        # Get all sectors with the max visit count and sort them
        result = [i for i in range(1, n + 1) if visit_count[i] == max_visit]

        return result

sol = Solution()
n = 4
rounds = [1,3,1,2]

print(sol.mostVisited(n, rounds))