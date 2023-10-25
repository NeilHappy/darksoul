#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        dup = set()
        while n not in dup:
            dup.add(n)
            str_n = str(n)
            new_num = 0
            for i in str_n:
                new_num += int(i)**2
            if new_num == 1:
                return True
            n = new_num
        return False


# @lc code=end
