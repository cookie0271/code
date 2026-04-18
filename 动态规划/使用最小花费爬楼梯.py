# 会超时的递归代码
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i: int) -> int:
            if i <= 1:  # 递归边界
                return 0
            return min(dfs(i - 1) + cost[i - 1], dfs(i - 2) + cost[i - 2])
        return dfs(len(cost))

