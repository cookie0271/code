class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int, j: int) -> int:
            if i == m - 1:  # 递归边界
                return grid[i][j]
            res = inf
            for k, c in enumerate(moveCost[grid[i][j]]):  # 移动到下一行的第 k 列
                res = min(res, dfs(i + 1, k) + c)
            return res + grid[i][j]

        return min(dfs(0, j) for j in range(n))  # 枚举起点

