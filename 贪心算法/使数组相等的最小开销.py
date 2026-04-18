class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        a = sorted(zip(nums, cost))
        s, mid = 0, (sum(cost) + 1) // 2
        for x, c in a:
            s += c
            if s >= mid:
                return sum(abs(y - x) * c for y, c in a)  # 把所有数都变成 x

