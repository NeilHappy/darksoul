#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

from collections import defaultdict

# @lc code=start


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        d = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                d[n1+n2] += 1

        count = 0
        for n3 in nums3:
            for n4 in nums4:
                target = -n3-n4
                count += d[target]
        return count


# @lc code=end
