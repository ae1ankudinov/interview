'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

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
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

# Time complexity - O(n) traverse all string
# Space complexity - O(1) since quantity of uniq characters is limited
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_idx = {}
        max_len = 0
        start_idx = 0
        for i in range(len(s)):
            if s[i] in last_idx.keys():
                start_idx = max(start_idx, last_idx[s[i]]+1)

            max_len = max(max_len, i-start_idx+1)
            last_idx[s[i]] = i

        return max_len



s = Solution()
s1 = 'abcabcbb'
out1 = 3
assert s.lengthOfLongestSubstring(s1) == out1
s2 = 'bbbbb'
out2 = 1
assert s.lengthOfLongestSubstring(s2) == out2
s3 = 'pwwkew'
out3 = 3
assert s.lengthOfLongestSubstring(s3) == out3
s4 = 'dvdf'
out4 = 3
assert s.lengthOfLongestSubstring(s4) == out4

