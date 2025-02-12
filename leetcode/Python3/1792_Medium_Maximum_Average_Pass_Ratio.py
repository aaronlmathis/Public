"""
There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.

You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.

The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:
Input: classes = [[1,2],[3,5],[2,2]], extraStudents = 2
Output: 0.78333
Explanation: You can assign the two extra students to the first class. The average pass ratio will be equal to (3/4 + 3/5 + 2/2) / 3 = 0.78333.

Example 2:
Input: classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
Output: 0.53485
 
"""
from typing import List
import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Create list full of tuples that contain ((negative) potential ratio, passing, total)
        classes = [(passing/total - (passing+1)/(total+1), passing, total) for passing, total in classes]
        # Create max heap
        heapq.heapify(classes)
        # Quick Exit
        if classes[0][0]==0:
            return 1
        # Iterate for each extra student, popping  class with the the max potential ratio
        # Add 1 student to passing and total for that class and push it back into the heap with updated potential ratio
        for i in range(extraStudents):
            _, passing, total = heapq.heappop(classes)
            heapq.heappush(classes, ((passing+1)/(total+1) - (passing+2)/(total+2), passing+1, total+1))

        # Return the sum of all ratios in classes divided by the number of classes (Average)
        return sum(passing / total for _, passing, total in classes) / len(classes)

classes = [[1,2],[3,5],[2,2]]
extraStudents = 2   
classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4     
sol = Solution()
print(sol.maxAverageRatio(classes, extraStudents))