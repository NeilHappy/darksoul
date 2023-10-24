# @before-stub-for-debug-begin
from python3problem3 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#


# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        values = set()
        left = 0
        result = 0
        for right, v in enumerate(s):
            while v in values:
                left_v = s[left]
                values.remove(left_v)
                left += 1
            values.add(v)
            result = max(result, right-left+1)
        return result


# @lc code=end
