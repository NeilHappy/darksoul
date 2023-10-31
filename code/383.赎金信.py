#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        result = [0]*26
        for i in magazine:
            result[ord(i)-ord('a')] += 1
        for i in ransomNote:
            result[ord(i)-ord('a')] -= 1
            if result[ord(i)-ord('a')] < 0:
                return False
        return True


# @lc code=end
