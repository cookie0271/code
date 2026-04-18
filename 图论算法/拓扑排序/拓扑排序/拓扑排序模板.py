# 返回有向无环图（DAG）的其中一个拓扑序
# 如果图中有环，返回空列表
# 节点编号从 0 到 n-1
def topologicalSort(n: int, edges: List[List[int]]) -> List[int]:
    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for x, y in edges:
        g[x].append(y)
        in_deg[y] += 1  # 统计 y 的先修课数量

    topo_order = []
    q = deque(i for i, d in enumerate(in_deg) if d == 0)  # 没有先修课，可以直接上
    while q:
        x = q.popleft()
        topo_order.append(x)
        for y in g[x]:
            in_deg[y] -= 1  # 修完 x 后，y 的先修课数量减一
            if in_deg[y] == 0:  # y 的先修课全部上完
                q.append(y)  # 加入学习队列

    if len(topo_order) < n:  # 图中有环
        return []
    return topo_order

