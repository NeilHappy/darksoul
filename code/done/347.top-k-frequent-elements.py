#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
import heapq
# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for item in nums:
            map_[item] = map_.get(item, 0) + 1

        # 小顶堆
        pre_que = []
        for key, freq in map_.items():
            heapq.heappush(pre_que, (freq, key))
            if len(pre_que) > k:
                heapq.heappop(pre_que)

        result = []
        for i in range(0, k):
            result.append(heapq.heappop(pre_que)[1])
        return result


# @lc code=end
