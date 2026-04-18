class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[inf for _ in range(n)] for _ in range(n)]  # 邻接矩阵
        for x, y, d in times:
            g[x - 1][y - 1] = d

        dis = [inf] * n
        ans = dis[k - 1] = 0
        done = [False] * n
        while True:
            x = -1
            for i, ok in enumerate(done):
                if not ok and (x < 0 or dis[i] < dis[x]):
                    x = i
            if x < 0:
                return ans  # 最后一次算出的最短路就是最大的
            if dis[x] == inf:  # 有节点无法到达
                return -1
            ans = dis[x]  # 求出的最短路会越来越大
            done[x] = True  # 最短路长度已确定（无法变得更小）
            for y, d in enumerate(g[x]):
                # 更新 x 的邻居的最短路
                dis[y] = min(dis[y], dis[x] + d)

