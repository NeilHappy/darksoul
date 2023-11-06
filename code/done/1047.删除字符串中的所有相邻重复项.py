#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if stack and item == stack[-1]:
                stack.pop()
            else:
                stack.append(item)
        return ''.join(stack)
# @lc code=end

