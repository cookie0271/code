class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        for i in range(n):
            state, unique, mn = [0] * n, 0, inf
            for j in range(i, -1, -1):
                x = nums[j]
                if state[x] == 0:  # 首次出现
                    state[x] = 1
                    unique += 1
                elif state[x] == 1:  # 不再唯一
                    state[x] = 2
                    unique -= 1
                mn = min(mn, f[j] - unique)
                # if f[j]-unique < mn: mn = f[j]-unique  # 手写 min 会快很多
            f[i + 1] = k + mn
        return f[n] + n

