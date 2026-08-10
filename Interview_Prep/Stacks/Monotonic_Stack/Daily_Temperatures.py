'''
https://leetcode.com/problems/daily-temperatures/description/
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
'''
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreasing_stack = [0]
        answers = [0 for i in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            top_temperature_index = decreasing_stack[-1]
            while temperatures[i] > temperatures[top_temperature_index] and len(decreasing_stack) > 0:
                top_temperature_index = decreasing_stack.pop()
                answers[top_temperature_index] = i - top_temperature_index
            decreasing_stack.append(i)
        return answers

s = Solution()
s.dailyTemperatures([73,74,75,71,69,72,76,73])