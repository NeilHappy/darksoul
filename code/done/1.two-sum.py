#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for index, v in enumerate(nums):
            rest = target - v
            if rest in d:
                return [d[rest], index]
            d[v] = index

# @lc code=end
