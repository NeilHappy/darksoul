#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        n = len(digits)
        if n == 0:
            return []
        path = ['']*n
        ans = []

        def dfs(i):
            if i == n:
                ans.append(''.join(path))
                return
            for c in MAPPING[int(digits[i])]:
                path[i] = c
                dfs(i+1)
        dfs(0)
        return ans


# @lc code=end
