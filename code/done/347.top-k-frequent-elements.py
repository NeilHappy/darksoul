#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
import heapq
from collections import defaultdict

# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = defaultdict(int)
        for item in nums:
            map_[item] += 1
        pri_que = []

        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        result = []
        for i in range(k):
            result.append(heapq.heappop(pri_que)[1])
        return result


# @lc code=end
