#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        length = len(nums)
        right = length - 1
        result = [0]*length
        for i in range(length-1, -1, -1):
            if nums[left]**2 >= nums[right]**2:
                result[i] = nums[left]**2
                left += 1
            else:
                result[i] = nums[right]**2
                right -= 1
        return result


# @lc code=end
