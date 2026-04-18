class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = s = 0  # 维护窗口元素和
        for i, x in enumerate(arr):
            # 1. 进入窗口
            s += x
            if i < k - 1:  # 窗口大小不足 k
                continue
            # 2. 更新答案
            if s >= k * threshold:
                ans += 1
            # 3. 离开窗口
            s -= arr[i - k + 1]
        return ans

