class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        # 记录每种字母的出现位置
        pos = defaultdict(list)
        for i, b in enumerate(s):
            pos[b].append(i)

        # 构建有向图
        g = defaultdict(list)
        for i, p in pos.items():
            l, r = p[0], p[-1]
            for j, q in pos.items():
                if j == i:
                    continue
                k = bisect_left(q, l)
                # [l, r] 包含第 j 个小写字母
                if k < len(q) and q[k] <= r:
                    g[i].append(j)

        # 遍历有向图
        def dfs(x: str) -> None:
            nonlocal l, r
            vis.add(x)
            p = pos[x]
            l = min(l, p[0])  # 合并区间
            r = max(r, p[-1])
            for y in g[x]:
                if y not in vis:
                    dfs(y)

        intervals = []
        for i, p in pos.items():
            # 如果要包含第 i 个小写字母，最终得到的区间是什么？
            vis = set()
            l, r = inf, 0
            dfs(i)
            intervals.append((l, r))

        # 435. 无重叠区间
        # 直接计算所选子串
        ans = []
        intervals.sort(key=lambda x: x[1])
        pre_r = -1
        for l, r in intervals:
            if l > pre_r:
                ans.append(s[l: r + 1])
                pre_r = r
        return ans
