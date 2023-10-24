#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#

from collections import defaultdict, Counter
# @lc code=start


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        cntMap = Counter()  # key是水果种类，不是index下标
        result = 0
        for right, v in enumerate(fruits):
            cntMap[v] += 1
            while len(cntMap) > 2:
                left_fruit = fruits[left]
                cntMap[left_fruit] -= 1
                if cntMap[left_fruit] == 0:
                    # del cntMap[left_fruit]
                    cntMap.pop(left_fruit)
                left += 1
            result = max(result, right-left+1)
        return result

# @lc code=end
