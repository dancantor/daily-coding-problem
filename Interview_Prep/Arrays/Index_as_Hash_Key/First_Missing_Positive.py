'''
https://leetcode.com/problems/first-missing-positive/
41. First Missing Positive
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
----------------------------------------------------------------------------------------------
The solution can't be greater than n
We don't care about negatives, 0 and numbers greater than n  + 1
so first we go through the array and for each of these 3 categories, we set the value to n + 2
the solution would be the first index where the value is not negative


[1 2 5]
[]
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for index, value in enumerate(nums):
            if value <= 0:
                nums[index] = N + 1
        for value in nums:
            index = abs(value) - 1
            if index < N:
                nums[index] = -abs(nums[index])

        for i in range(N):
            if nums[i] > 0:
                return i + 1
        return N + 1
        


        