class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        g = [[inf] * n for _ in range(n)]
        for x, y, wt in roads:
            g[x][y] = min(g[x][y], wt)
            g[y][x] = min(g[y][x], wt)

        f = [None] * n
        def check(s: int) -> int:
            for i, row in enumerate(g):
                if s >> i & 1:  # i 在集合 s 中
                    f[i] = row.copy()

            # Floyd 算法（只考虑在 s 中的节点）
            for k in range(n):
                if (s >> k & 1) == 0:  # k 不在集合 s 中
                    continue
                for i in range(n):
                    if (s >> i & 1) == 0 or f[i][k] == inf:
                        continue
                    for j in range(n):
                        f[i][j] = min(f[i][j], f[i][k] + f[k][j])

            # 判断保留的节点之间的最短路是否均不超过 maxDistance
            for i, di in enumerate(f):
                if (s >> i & 1) == 0:  # i 不在集合 s 中
                    continue
                for j, dij in enumerate(di[:i]):
                    if s >> j & 1 and dij > maxDistance:
                        return 0
            return 1

        # 枚举子集 s，作为保留的节点，判断这些节点否满足要求
        return sum(check(s) for s in range(1 << n))
