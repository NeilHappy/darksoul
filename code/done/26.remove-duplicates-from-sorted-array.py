#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right, v in enumerate(nums):
            if left == right:
                continue
            if v != nums[left]:
                left += 1
                nums[left] = v
        return left+1


# @lc code=end
