#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = dict()
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            next = dp[1] + dp[2]
            dp[1] = dp[2]
            dp[2] = next
        return dp[2]


# @lc code=end
