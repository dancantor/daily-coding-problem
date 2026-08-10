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
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answers = [0 for i in range(len(temperatures))]
        i = len(temperatures) - 2
        while i >= 0:
            j = i + 1
            if temperatures[i] < temperatures[j]:
                answers[i] = 1
            elif temperatures[i] == temperatures[j]:
                answers[i] = 0 if answers[j] == 0 else answers[j] + 1
            else:
                while temperatures[i] >= temperatures[j]:
                    if answers[j] == 0:
                        j = -1
                        break
                    j += answers[j]
                answers[i] = 0 if j == -1 else j - i
            i -= 1
        return answers

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        decreasing_stack = [0]
        answers = [0 for i in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            while decreasing_stack and  temperatures[i] > temperatures[decreasing_stack[-1]]:
                top_temperature_index = decreasing_stack.pop()
                answers[top_temperature_index] = i - top_temperature_index
            decreasing_stack.append(i)
        return answers