class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans, s, i = 0, 1, 0
        while s <= n:
            if i < len(nums) and nums[i] <= s:
                s += nums[i]
                i += 1
            else:
                s *= 2  # 必须添加 s
                ans += 1
        return ans
