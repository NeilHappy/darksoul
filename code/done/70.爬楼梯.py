#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0]*2
        dp[0] = 1
        dp[1] = 2

        for i in range(3, n+1):
            temp = dp[1]
            dp[1] = dp[1] + dp[0]
            dp[0] = temp
        return dp[1]


# @lc code=end
