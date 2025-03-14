"""
There is a bookstore owner that has a store open for n minutes. You are given an integer array customers of length n where
customers[i] is the number of the customers that enter the store at the start of the ith minute and all those customers leave after the end of that minute.

During certain minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, 
and is 0 otherwise.

When the bookstore owner is grumpy, the customers entering during that minute are not satisfied. Otherwise, they are satisfied.
The bookstore owner knows a secret technique to remain not grumpy for minutes consecutive minutes, but this technique can only be used once.
Return the maximum number of customers that can be satisfied throughout the day.

Example 1:
Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
Output: 16
Explanation:
The bookstore owner keeps themselves not grumpy for the last 3 minutes.
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Example 2:
Input: customers = [1], grumpy = [0], minutes = 1
Output: 1

"""
from typing import List

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #Find the initial satisfied customer list.
        starting_satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)

        #find the additional satisfaction of the first window size of Minutes
        additional_statisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_statisfied+=customers[i]
        #slide the window one place to the right until end of list.
        max_add_satisfied = additional_statisfied
        for i in range(minutes, len(customers)):
            print(i)
            if grumpy[i] == 1:
                additional_statisfied+=customers[i]
            if grumpy[i - minutes] == 1:
                additional_statisfied -=customers[i-minutes]

            max_add_satisfied = max(max_add_satisfied, additional_statisfied)
        
        return starting_satisfied + max_add_satisfied
        

customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
minutes = 3
sol = Solution()
print(sol.maxSatisfied(customers, grumpy, minutes))
customers = [1]
grumpy = [0]
minutes = 1
print(sol.maxSatisfied(customers, grumpy, minutes))