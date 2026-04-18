class Solution:
    def movesToMakeZigzag(self, nums):
        s = [0] * 2
        for i, x in enumerate(nums):
            left = nums[i - 1] if i else inf
            right = nums[i + 1] if i < len(nums) - 1 else inf
            s[i % 2] += max(x - min(left, right) + 1, 0)
        return min(s)

