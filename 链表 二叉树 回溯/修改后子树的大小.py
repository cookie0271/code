class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)

        ancestor = defaultdict(lambda: -1)
        def rebuild(x: int) -> None:
            old = ancestor[s[x]]
            ancestor[s[x]] = x
            for i in range(len(g[x])):
                y = g[x][i]
                if (anc := ancestor[s[y]]) != -1:
                    g[anc].append(y)
                    g[x][i] = -1  # -1 表示删除 y
                rebuild(y)
            ancestor[s[x]] = old  # 恢复现场
        rebuild(0)

        size = [1] * n  # 注意这里已经把 1 算进去了
        def dfs(x: int) -> None:
            for y in g[x]:
                if y != -1:  # y 没被删除
                    dfs(y)
                    size[x] += size[y]
        dfs(0)
        return size

