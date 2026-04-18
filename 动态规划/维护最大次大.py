class Solution:
    def maxSubgraphScore(self, n: int, edges: List[List[int]], good: List[int]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # sub_score[x] 表示（以 0 为根时）包含 x 的子树 x 的最大得分
        sub_score = [0] * n
        # 计算 sub_score[x]
        def dfs(x: int, fa: int) -> None:
            sub_score[x] = 1 if good[x] else -1  # sub_score[x] 一定包含 x
            for y in g[x]:
                if y != fa:
                    dfs(y, x)
                    # 如果子树 y 的最大得分 > 0，选子树 y，否则不选
                    sub_score[x] += max(sub_score[y], 0)
        dfs(0, -1)

        ans = [0] * n
        ans[0] = sub_score[0]
        # 对于 x 的儿子 y，计算包含 y 的子图最大得分
        def reroot(x: int, fa: int) -> None:
            for y in g[x]:
                if y != fa:
                    # 从 ans[x] 中去掉子树 y，剩余部分记作 F
                    score_f = ans[x] - max(sub_score[y], 0)
                    # 换根后，x 挂在 y 的下面，F 变成 y 的一棵子树
                    # 计算 F 对 y 的贡献：如果 F 的最大得分 > 0，选 F，否则不选
                    ans[y] = sub_score[y] + max(score_f, 0)
                    reroot(y, x)
        reroot(0, -1)
        return ans
