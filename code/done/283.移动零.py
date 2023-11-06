#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right, v in enumerate(nums):
            if v !=0:
                nums[left] = nums[right]
                left+=1
        for i in range(left, len(nums)):
            nums[i] = 0
# @lc code=end

