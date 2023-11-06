#
# @lc app=leetcode.cn id=454 lang=python3
#
# [454] 四数相加 II
#
from collections import defaultdict

# @lc code=start
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        dup = defaultdict(int)
        for i in nums1:
            for j in nums2:
                dup[i+j]+=1
                
        count = 0
        for k in nums3:
            for l in nums4:
                v = -k-l
                if v in dup:
                    count+=dup[v]
        return count
# @lc code=end

