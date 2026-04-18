class Solution:
    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        total = Counter(nums) + Counter(forbidden)
        if any(c > n for c in total.values()):
            return -1

        same = Counter(x for x, y in zip(nums, forbidden) if x == y)
        k = same.total()
        mx = max(same.values(), default=0)
        return max((k + 1) // 2, mx)

