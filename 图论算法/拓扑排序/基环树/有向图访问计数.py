class Solution:
    def countVisitedNodes(self, g: List[int]) -> List[int]:
        n = len(g)
        rg = [[] for _ in range(n)]  # 反图
        deg = [0] * n
        for x, y in enumerate(g):
            rg[y].append(x)
            deg[y] += 1

        # 拓扑排序，剪掉 g 上的所有树枝
        # 拓扑排序后，deg 值为 1 的点必定在基环上，为 0 的点必定在树枝上
        q = deque(i for i, d in enumerate(deg) if d == 0)
        while q:
            x = q.popleft()
            y = g[x]
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)

        ans = [0] * n
        # 在反图上遍历树枝
        def rdfs(x: int, depth: int) -> None:
            ans[x] = depth
            for y in rg[x]:
                if deg[y] == 0:  # 树枝上的点在拓扑排序后，入度均为 0
                    rdfs(y, depth + 1)
        for i, d in enumerate(deg):
            if d <= 0:
                continue
            ring = []
            x = i
            while True:
                deg[x] = -1  # 将基环上的点的入度标记为 -1，避免重复访问
                ring.append(x)  # 收集在基环上的点
                x = g[x]
                if x == i:
                    break
            for x in ring:
                rdfs(x, len(ring))  # 为方便计算，以 len(ring) 作为初始深度
        return ans

