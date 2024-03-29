from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in nums:
            result = result ^ i
        return result


s = Solution()
print(s.singleNumber([4, 1, 2, 1, 2]))
