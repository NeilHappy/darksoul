#
# @lc app=leetcode id=904 lang=python3
#
# [904] Fruit Into Baskets
#
from collections import defaultdict

# @lc code=start


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        cnt = defaultdict(int)
        result = 0
        for right, v in enumerate(fruits):
            cnt[v] += 1
            while len(cnt) > 2:
                y = fruits[left]
                cnt[y] -= 1
                if cnt[y] == 0:
                    del cnt[y]
                left += 1
            result = max(result, right-left+1)
        return result


# @lc code=end
