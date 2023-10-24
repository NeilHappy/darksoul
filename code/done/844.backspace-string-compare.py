#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.getCleanStr(s) == self.getCleanStr(t)

    def getCleanStr(self, s: str) -> str:
        result = [''] * len(s)
        slow = 0
        for fast in range(len(s)):
            if s[fast] != '#':
                result[slow] = s[fast]
                slow += 1
            else:
                if slow > 0:
                    slow -= 1
        return str(result[:slow])
"""


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(s: str) -> str:
            result = list()
            for ch in s:
                if ch != '#':
                    result.append(ch)
                else:
                    if len(result) > 0:
                        result.pop()
            return "".join(result)

        return build(s) == build(t)

# @lc code=end
