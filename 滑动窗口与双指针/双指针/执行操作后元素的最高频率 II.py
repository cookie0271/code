class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        n = len(nums)
        ans = cnt = left = right = 0
        for i, x in enumerate(nums):
            cnt += 1
            # 循环直到连续相同段的末尾，这样可以统计出 x 的出现次数
            if i < n - 1 and x == nums[i + 1]:
                continue
            while nums[left] < x - k:
                left += 1
            while right < n and nums[right] <= x + k:
                right += 1
            ans = max(ans, min(right - left, cnt + numOperations))
            cnt = 0

        if ans >= numOperations:
            return ans

        left = 0
        for right, x in enumerate(nums):
            while nums[left] < x - k * 2:
                left += 1
            ans = max(ans, right - left + 1)
        return min(ans, numOperations)  # 最后和 numOperations 取最小值

