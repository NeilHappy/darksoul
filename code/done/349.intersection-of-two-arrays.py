#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = list[int]()
        set1 = set(nums1)
        set2 = set(nums2)
        for num in set1:
            if num in set2:
                ret.append(num)

        return ret

# @lc code=end
