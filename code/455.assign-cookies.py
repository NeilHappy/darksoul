#
# @lc app=leetcode id=455 lang=python3
#
# [455] Assign Cookies
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        index_s = len(s)-1
        result = 0
        for index_g in range(len(g)-1, -1, -1):
            if index_s < 0:
                break
            if s[index_s] >= g[index_g]:
                result += 1
                index_s -= 1
        return result


# @lc code=end
