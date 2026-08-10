'''
https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/

1944. Number of Visible People in a Queue
Hard
Topics
premium lock icon
Companies
Hint
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

 

Example 1:



Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Explanation:
Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.
Example 2:

Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]
 

Constraints:
n == heights.length
1 <= n <= 105
1 <= heights[i] <= 105
All the values of heights are unique.
'''

from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        nr_visible = [0 for i in range(len(heights))]
        monotonic_stack = [heights[-1]]
        i = len(heights) - 2
        while i >= 0:
            cur_value = heights[i]
            cur_people = 0
            while monotonic_stack and cur_value > monotonic_stack[-1]:
                cur_people += 1
                monotonic_stack.pop()
            if monotonic_stack:
                cur_people += 1
            nr_visible[i] = cur_people
            monotonic_stack.append(cur_value)
            i -= 1
        return nr_visible