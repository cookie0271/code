class Solution:
    def timeTaken(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # sub_res[x] 保存子树 x 的最大深度，次大深度，以及最大深度要往哪个儿子走
        sub_res = [None] * n
        # 计算 sub_res[x]
        def dfs(x: int, fa: int) -> None:
            max_d = max_d2 = my = 0
            for y in g[x]:
                if y == fa:
                    continue
                dfs(y, x)
                w = 2 - y % 2  # 从 x 到 y 的边权
                max_y = sub_res[y][0] + w  # 从 x 出发，往 y 方向的最大深度
                if max_y > max_d:
                    max_d2 = max_d
                    max_d = max_y
                    my = y
                elif max_y > max_d2:
                    max_d2 = max_y
            sub_res[x] = (max_d, max_d2, my)
        dfs(0, -1)

        # ans[x] 表示当 x 是树根时，整棵树的最大深度
        ans = [0] * n
        # 计算 ans[x]
        def reroot(x: int, fa: int, from_up: int) -> None:
            max_d, max_d2, my = sub_res[x]
            ans[x] = max(max_d, from_up)
            for y in g[x]:
                if y == fa:
                    continue
                w = 2 - x % 2  # 从 y 到 x 的边权
                mx = max_d if y != my else max_d2
                # 站在 x 的角度，不往 y 走，能走多远？
                # 要么往上走（from_up），要么往除了 y 的其余子树走（mx），二者取最大值
                reroot(y, x, max(from_up, mx) + w)  # 对于 y 来说，加上从 y 到 x 的边权 w
        reroot(0, -1, 0)
        return ans

