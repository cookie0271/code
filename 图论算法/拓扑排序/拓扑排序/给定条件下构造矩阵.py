class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(edges: List[List[int]]) -> List[int]:
            g = [[] for _ in range(k)]
            in_deg = [0] * k
            for x, y in edges:
                g[x - 1].append(y - 1)  # 顶点编号从 0 开始，方便计算
                in_deg[y - 1] += 1
            order = []
            q = deque(i for i, d in enumerate(in_deg) if d == 0)
            while q:
                x = q.popleft()
                order.append(x)
                for y in g[x]:
                    in_deg[y] -= 1
                    if in_deg[y] == 0:
                        q.append(y)
            return order if len(order) == k else None

        if (row := topo_sort(rowConditions)) is None or (col := topo_sort(colConditions)) is None:
            return []
        pos = {x: i for i, x in enumerate(col)}
        ans = [[0] * k for _ in range(k)]
        for i, x in enumerate(row):
            ans[i][pos[x]] = x + 1
        return ans

