#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

from operator import add, sub, mul
# @lc code=start


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x/y)}
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op_map[token](op1, op2))
        return stack.pop()
# @lc code=end
