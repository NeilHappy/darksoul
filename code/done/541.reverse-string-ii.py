#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        for i in range(0, len(s), 2*k):
            l[i:i+k] = reversed(l[i:i+k])
        return "".join(l)


# @lc code=end
