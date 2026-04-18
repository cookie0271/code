class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        g = [[] for _ in range(len(roads) + 1)]
        for x, y in roads:
            g[x].append(y)  # 记录每个点的邻居
            g[y].append(x)

        ans = 0
        def dfs(x: int, fa: int) -> int:
            size = 1
            for y in g[x]:
                if y != fa:  # 递归子节点，不能递归父节点
                    size += dfs(y, x)  # 统计子树大小
            if x:  # x 不是根节点
                nonlocal ans
                ans += (size - 1) // seats + 1  # ceil(size/seats)
            return size
        dfs(0, -1)
        return ans

