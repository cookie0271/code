class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n:
            start = i
            ones = nums[i].bit_count()
            i += 1
            while i < n and nums[i].bit_count() == ones:
                i += 1
            nums[start:i] = sorted(nums[start:i])
        return all(x <= y for x, y in pairwise(nums))

