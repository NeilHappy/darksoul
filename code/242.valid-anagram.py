#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = [0]*26
        for ch in s:
            d[ord(ch)-ord('a')] += 1
        for ch in t:
            d[ord(ch)-ord('a')] -= 1
        return d == [0]*26


# @lc code=end
