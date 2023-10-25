#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = [0]*26
        for ch in magazine:
            d[ord(ch)-ord('a')] += 1
        for ch in ransomNote:
            d[ord(ch)-ord('a')] -= 1
            if d[ord(ch)-ord('a')] < 0:
                return False
        return True

# @lc code=end
