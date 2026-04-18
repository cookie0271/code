# 首先寻找子问题
# 然后进行状态定义和状态转移方程
# 直接用记忆化搜索

DIRS = (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(k: int, i: int, j: int) -> float:
            if not (0 <= i < n and 0 <= j < n):  # 出界
                return 0
            if k == 0:  # 走完了，仍然在棋盘上
                return 1
            return sum(dfs(k - 1, i + dx, j + dy) for dx, dy in DIRS) / 8
        return dfs(k, row, column)
# 1:1 翻译成递推
DIRS = (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        f = [[[0] * (n + 4) for _ in range(n + 4)] for _ in range(k + 1)]
        for i in range(2, n + 2):
            f[0][i][2: n + 2] = [1] * n
        for step in range(1, k + 1):
            for i in range(2, n + 2):
                for j in range(2, n + 2):
                    f[step][i][j] = sum(f[step - 1][i + dx][j + dy] for dx, dy in DIRS) / 8
        return f[k][row + 2][column + 2]

