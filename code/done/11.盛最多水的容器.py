#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0
        while l < r:
            area = (r-l)*min(height[l], height[r])
            ans = max(ans, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans


# @lc code=end
