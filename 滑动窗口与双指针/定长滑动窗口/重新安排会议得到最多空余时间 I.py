class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        free = [0] * (n + 1)
        free[0] = startTime[0]  # 最左边的空余时间段
        for i in range(1, n):
            free[i] = startTime[i] - endTime[i - 1]  # 中间的空余时间段
        free[n] = eventTime - endTime[-1]  # 最右边的空余时间段

        # 套定长滑窗模板（窗口长为 k+1）
        ans = s = 0
        for i, f in enumerate(free):
            s += f
            if i < k:
                continue
            ans = max(ans, s)
            s -= free[i - k]
        return ans

