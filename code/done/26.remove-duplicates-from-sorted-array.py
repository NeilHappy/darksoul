#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        for fast, num in enumerate(nums[1:], start=1):
            if nums[slow] == nums[fast]:
                continue
            else:
                slow += 1
                nums[slow] = nums[fast]

        return slow+1


# @lc code=end
