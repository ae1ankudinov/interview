'''
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

# Time complexity - O(n^2)
# Space complexity - O(1)
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Time complexity - O(n)
# Space complexity - O(n)
class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        nums_dict = {}
        for num, val in enumerate(nums):
            dif = target-val
            if dif in nums_dict.keys():
                return [nums_dict[dif], num]
            else:
                nums_dict[val] = num


s = Solution()
nums1, target1, out1 = [2, 7, 11, 15], 9, [0, 1]
assert s.twoSum(nums1, target1) == out1
nums2, target2, out2 = [3, 2, 4], 6, [1, 2]
assert s.twoSum(nums2, target2) == out2
nums3, target3, out3 = [3, 3], 6, [0, 1]
assert s.twoSum(nums3, target3) == out3

