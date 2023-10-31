#
# @lc app=leetcode.cn id=844 lang=python3
#
# [844] 比较含退格的字符串
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.getCleanStr(s) == self.getCleanStr(t)

    def getCleanStr(self, s: str) -> str:
        t = list(s)
        left = 0
        for right, v in enumerate(s):
            if v == '#':
                if left > 0:
                    left -= 1
            else:
                t[left] = s[right]
                left += 1
        return "".join(t[:left])
        """
        stack = []
        for ch in s:
            if stack and ch == '#':
                stack.pop()
            elif ch != '#':
                stack.append(ch)
        return "".join(stack)
        """


# @lc code=end
