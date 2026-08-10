'''
https://leetcode.com/problems/minimum-window-substring/description/

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        char_freq = {}
        remaining_chars = len(t)

        for char in t:
            char_freq[char] = char_freq.get(char, 0) + 1

        left = 0
        min_length = len(s) + 1
        min_left = 0
        min_right = 0
        for right in range(len(s)):
            if s[right] in char_freq:
                if char_freq[s[right]] > 0:
                    remaining_chars -= 1
                char_freq[s[right]] -= 1
            
            while remaining_chars == 0:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_left = left
                    min_right = right
                if s[left] not in char_freq:
                    left += 1
                    continue

                char_freq[s[left]] += 1
                if char_freq[s[left]] > 0:
                    remaining_chars += 1
                left += 1
        return "" if min_length == len(s) + 1 else s[min_left:min_right + 1]


        
        