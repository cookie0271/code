class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # colors[i] = 0  表示未访问节点 i
        # colors[i] = 1  表示节点 i 为红色
        # colors[i] = -1 表示节点 i 为蓝色
        colors = [0] * len(graph)

        def dfs(x: int, c: int) -> bool:
            colors[x] = c  # 节点 x 染成颜色 c
            for y in graph[x]:
                # 邻居 y 的颜色与 x 的相同，说明不是二分图，返回 False
                # 或者继续递归，发现不是二分图，返回 False
                if colors[y] == c or \
                   colors[y] == 0 and not dfs(y, -c):  # 取相反数，实现交替染色
                    return False
            return True

        # 可能有多个连通块
        for i, c in enumerate(colors):
            if c == 0 and not dfs(i, 1):
                # 从节点 i 开始递归，发现 i 所在连通块不是二分图
                return False
        return True

