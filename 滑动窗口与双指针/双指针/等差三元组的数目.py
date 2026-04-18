class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans, i, j = 0, 0, 1
        for x in nums:  # x = nums[k]
            while nums[j] + diff < x:
                j += 1
            if nums[j] + diff > x:
                continue
            while nums[i] + diff * 2 < x:
                i += 1
            if nums[i] + diff * 2 == x:
                ans += 1
        return ans

