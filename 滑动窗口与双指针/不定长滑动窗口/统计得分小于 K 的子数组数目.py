class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = s = left = 0
        for right, x in enumerate(nums):
            s += x
            while s * (right - left + 1) >= k:
                s -= nums[left]
                left += 1
            ans += right - left + 1
        return ans

