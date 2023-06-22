import heapq
from heapq import heapify, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_d = {}
        arr = []
        result = []

        for i in nums:
            if i in freq_d:
                freq_d[i] += 1
            else:
                freq_d[i] = 1

        for ele in freq_d.keys():
            arr.append((-freq_d[ele], ele))
        heapify(arr)
        # heapq._heapify_max(arr)

        for i in range(k):
            result.append(heappop(arr)[1])
            # result.append(heapq._heappop_max(arr)[1])
        return result


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))

