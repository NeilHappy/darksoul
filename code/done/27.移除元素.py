#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        for right, v in enumerate(nums):
            if v == val:
                continue
            else:
                nums[slow] = nums[right]
                slow+=1
        return slow

# @lc code=end

