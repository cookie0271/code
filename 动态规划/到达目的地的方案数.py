class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = [[inf for _ in range(n)] for _ in range(n)]  # 邻接矩阵
        for x, y, d in roads:
            g[x][y] = g[y][x] = d

        dis = [inf] * n
        dis[0] = 0
        f = [0] * n
        f[0] = 1
        done = [False] * n
        while True:
            x = -1
            for i, ok in enumerate(done):
                if not ok and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x == n - 1:
                # 不可能找到比 dis[-1] 更短，或者一样短的最短路了（注意本题边权都是正数）
                return f[-1]
            done[x] = True  # 最短路长度已确定（无法变得更小）
            dx = dis[x]
            for y, d in enumerate(g[x]):  # 尝试更新 x 的邻居的最短路
                new_dis = dx + d
                if new_dis < dis[y]:
                    # 就目前来说，最短路必须经过 x
                    dis[y] = new_dis
                    f[y] = f[x]
                elif new_dis == dis[y]:
                    # 和之前求的最短路一样长
                    f[y] = (f[y] + f[x]) % 1_000_000_007

