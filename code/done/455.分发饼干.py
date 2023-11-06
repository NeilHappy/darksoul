#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        j = len(s)-1
        count=0
        for i in range(len(g)-1,-1,-1):
            if j < 0:
                break
            if g[i] <= s[j]:
                count+=1
                j-=1
        return count
                
            

# @lc code=end

