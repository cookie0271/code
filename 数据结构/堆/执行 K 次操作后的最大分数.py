class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heapify_max(nums)  # 原地堆化
        ans = 0
        for _ in range(k):
            ans += heapreplace_max(nums, (nums[0] + 2) // 3)
        return ans

