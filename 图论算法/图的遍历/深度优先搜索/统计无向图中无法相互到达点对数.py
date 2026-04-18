class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建图

        vis = [False] * n
        def dfs(x: int) -> int:
            vis[x] = True  # 避免重复访问同一个点
            size = 1
            for y in g[x]:
                if not vis[y]:
                    size += dfs(y)
            return size

        ans = total = 0
        for i in range(n):
            if not vis[i]:  # 未访问的点：说明找到了一个新的连通块
                size = dfs(i)
                ans += size * total
                total += size
        return ans
