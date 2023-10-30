# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        dup = set()
        result = 0
        for right, v in enumerate(s):
            while v in dup:
                dup.remove(s[left])
                left += 1
            dup.add(v)
            result = max(result, right-left+1)
        return result


# @lc code=end
