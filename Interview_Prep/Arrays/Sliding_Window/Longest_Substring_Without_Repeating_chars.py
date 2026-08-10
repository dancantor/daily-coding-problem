'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 105
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        max_length = 0
        cur_length = 0
        freq_array = {}
        if len(s) == 0:
            return 0
        while j < len(s):
            if s[j] not in freq_array or freq_array[s[j]] == 0:
                freq_array[s[j]] = 1
            else:
                while freq_array[s[j]] == 1:
                    freq_array[s[i]] = 0
                    cur_length -= 1
                    i += 1
                freq_array[s[j]] = 1
            j += 1
            cur_length += 1
            if cur_length > max_length:
                max_length = cur_length
        return max_length
            
            