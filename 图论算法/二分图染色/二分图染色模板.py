# 返回图的二染色
# 如果是二分图，返回每个节点的颜色，用 1 和 2 表示两种颜色
# 如果不是二分图，返回空列表
# 时间复杂度 O(n+m)，n 是点数，m 是边数
def colorBipartite(n: int, edges: List[List[int]]) -> List[int]:
    # 建图（节点编号从 0 到 n-1）
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)

    # colors[i] = 0 表示未访问节点 i
    # colors[i] = 1 表示节点 i 为红色
    # colors[i] = 2 表示节点 i 为蓝色
    colors = [0] * n

    def dfs(x: int, c: int) -> bool:
        colors[x] = c  # 节点 x 染成颜色 c
        for y in g[x]:
            # 邻居 y 的颜色与 x 的相同，说明不是二分图，返回 False
            # 或者继续递归，发现不是二分图，返回 False
            if colors[y] == c or \
               colors[y] == 0 and not dfs(y, 3 - c):  # 1 和 2 交替染色
                return False
        return True

    # 可能有多个连通块
    for i, c in enumerate(colors):
        if c == 0 and not dfs(i, 1):
            # 从节点 i 开始递归，发现 i 所在连通块不是二分图
            return []
    return colors

