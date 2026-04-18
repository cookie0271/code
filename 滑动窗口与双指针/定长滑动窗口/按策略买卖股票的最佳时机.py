# 手写 max 更快
max = lambda a, b: b if b > a else a

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        total = s = 0
        # 计算第一个窗口的 s
        for p, st in zip(prices[:k // 2], strategy[:k // 2]):
            total += p * st
            s -= p * st
        for p, st in zip(prices[k // 2: k], strategy[k // 2: k]):
            total += p * st
            s += p * (1 - st)

        max_s = max(s, 0)
        # 向右滑动，计算后续窗口的 s
        for i in range(k, len(prices)):
            p, st = prices[i], strategy[i]
            total += p * st
            s += p * (1 - st) - prices[i - k // 2] + prices[i - k] * strategy[i - k]
            max_s = max(max_s, s)
        return total + max_s

