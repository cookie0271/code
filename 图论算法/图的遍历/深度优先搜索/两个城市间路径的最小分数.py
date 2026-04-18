class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for x, y, d in roads:
            g[x - 1].append((y - 1, d))
            g[y - 1].append((x - 1, d))
        ans = inf
        vis = [False] * n
        def dfs(x: int) -> None:
            nonlocal ans
            vis[x] = True
            for y, d in g[x]:
                ans = min(ans, d)
                if not vis[y]:
                    dfs(y)
        dfs(0)
        return ans

