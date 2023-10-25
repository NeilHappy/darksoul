#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dup = set()
        result = 0
        for right, v in enumerate(s):
            while v in dup:
                left_v = s[left]
                dup.remove(left_v)
                left += 1
            dup.add(v)
            result = max(result, right-left+1)
        return result

# @lc code=end
