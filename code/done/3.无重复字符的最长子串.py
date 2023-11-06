#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        left = 0
        result = 0
        for right, v in enumerate(s):
            while v in dup:
                left_v = s[left]
                dup.remove(left_v)
                left+=1
            dup.add(v)
            result = max(result, right-left+1)
        return result
# @lc code=end

