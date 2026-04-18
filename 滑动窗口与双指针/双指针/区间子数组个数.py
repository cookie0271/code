class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, i0, i1 = 0, -1, -1
        for i, x in enumerate(nums):
            if x > right: i0 = i
            if x >= left: i1 = i
            ans += i1 - i0
        return ans

