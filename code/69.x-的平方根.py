#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        while left < right:
            mid = (left+right)//2
            s = mid**2
            if s == x:
                return mid
            elif s > x:
                right = mid
            else:
                left = mid+1
        return left-1

# @lc code=end
