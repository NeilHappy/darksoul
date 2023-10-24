#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            str_n = str(n)
            new_n = 0
            for i in str_n:
                new_n += int(i)**2
            if new_n == 1:
                return True
            n = new_n
        return False


# @lc code=end
