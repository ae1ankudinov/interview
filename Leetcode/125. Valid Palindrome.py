'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''


# Time complexity - O(n) + O(n/2) => O(n)
# Space complexity - O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s.lower() if i.isalnum())
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True


# Time complexity - O(n/2) => O(n)
# Space complexity - O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1

            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True


s = Solution()
s1 = "A man, a plan, a canal: Panama"
assert s.isPalindrome(s1) is True
s2 = "race a car"
assert s.isPalindrome(s2) is False
s3 = " "
assert s.isPalindrome(s3) is True
