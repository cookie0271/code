class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[i + 1] for i in range(n - 1)]
        vis = [-1] * (n - 1)

        def bfs(i: int) -> int:
            q = [0]
            for step in count(1):
                tmp = q
                q = []
                for x in tmp:
                    for y in g[x]:
                        if y == n - 1:
                            return step
                        if vis[y] != i:
                            vis[y] = i
                            q.append(y)
            return -1

        ans = [0] * len(queries)
        for i, (l, r) in enumerate(queries):
            g[l].append(r)
            ans[i] = bfs(i)
        return ans

