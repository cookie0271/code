class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        groups = defaultdict(list)
        for lim, v in zip(limit, value):
            groups[lim].append(v)

        ans = 0
        for lim, a in groups.items():
            # 取最大的 lim 个数。更快写法见【Python3 优化】
            a.sort()
            ans += sum(a[-lim:])
        return ans

