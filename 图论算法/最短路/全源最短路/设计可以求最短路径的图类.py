class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        f = [[inf] * n for _ in range(n)]
        for i in range(n):
            f[i][i] = 0
        for x, y, w in edges:
            f[x][y] = w  # 添加一条边（题目保证没有重边和自环）
        for k in range(n):
            for i in range(n):
                if f[i][k] == inf: continue
                for j in range(n):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j])
        self.f = f

    def addEdge(self, edge: List[int]) -> None:
        f = self.f
        x, y, w = edge
        if w >= f[x][y]:  # 无需更新
            return
        n = len(f)
        for i in range(n):
            for j in range(n):
                f[i][j] = min(f[i][j], f[i][x] + w + f[y][j])

    def shortestPath(self, start: int, end: int) -> int:
        ans = self.f[start][end]
        return ans if ans < inf else -1

