#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0, 1]
        for i in range(2, n+1):
            next = dp[0] + dp[1]
            dp[0] = dp[1]
            dp[1] = next
        return dp[1]


# @lc code=end
