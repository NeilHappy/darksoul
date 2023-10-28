#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

from operator import add, sub, mul

# @lc code=start


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {'+': add, '-': sub, '*': mul, '/': lambda x, y: int(x/y)}
        result = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                result.append(int(token))
            else:
                op2 = result.pop()
                op1 = result.pop()
                result.append(op_map[token](op1, op2))
        return result.pop()


# @lc code=end
