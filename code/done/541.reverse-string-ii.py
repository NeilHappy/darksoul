#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse_str(t: list[int]) -> list[int]:
            left, right = 0, len(t)-1
            while left < right:
                t[left], t[right] = t[right], t[left]
                left += 1
                right -= 1
            return t
        t = list(s)
        for i in range(0, len(s), 2*k):
            t[i:i+k] = reverse_str(t[i:i+k])
        return "".join(t)


class Solution:
    def replaceSpace(self, s: str) -> str:
        counter = s.count(' ')
        res = list(s)
        res.extend([' ']*counter*2)

        left, right = len(s)-1, len(res)-1
        while left > 0:
            if res[left] != ' ':
                res[right] = s[left]
                right -= 1
            else:
                res[right-2, right+1] = "%20"
                right -= 3
            left -= 1
        return "".join(res)

# @lc code=end
