#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        result = len(nums)+1
        for right, v in enumerate(nums):
            sum += v
            while sum >= target:
                result = min(result, right-left+1)
                sum -= nums[left]
                left += 1
        # if result == len(nums) + 1:
        #    return 0
        return result if result <= len(nums) else 0

# @lc code=end
