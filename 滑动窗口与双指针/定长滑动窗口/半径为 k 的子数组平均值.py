class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = [-1] * len(nums)
        s = 0  # 维护窗口元素和
        for i, x in enumerate(nums):
            # 1. 进入窗口
            s += x
            if i < k * 2:  # 窗口大小不足 2k+1
                continue
            # 2. 记录答案
            avgs[i - k] = s // (k * 2 + 1)
            # 3. 离开窗口
            s -= nums[i - k * 2]
        return avgs

