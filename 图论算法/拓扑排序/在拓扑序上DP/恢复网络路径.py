class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        deg = [0] * n
        max_wt = -1
        for x, y, wt in edges:
            if online[x] and online[y]:
                g[x].append((y, wt))
                deg[y] += 1
                if x == 0:
                    max_wt = max(max_wt, wt)

        # 先清理无法从 0 到达的边
        q = deque(i for i in range(1, n) if deg[i] == 0)
        while q:
            x = q.popleft()
            for y, _ in g[x]:
                deg[y] -= 1
                if y and deg[y] == 0:
                    q.append(y)

        def check(lower: int) -> bool:
            deg_copy = deg.copy()
            f = [inf] * n
            f[0] = 0

            q = deque([0])
            while q:
                x = q.popleft()
                if x == n - 1:
                    return f[x] > k
                for y, wt in g[x]:
                    if wt >= lower:
                        f[y] = min(f[y], f[x] + wt)
                    deg_copy[y] -= 1
                    if deg_copy[y] == 0:
                        q.append(y)
            return True

        # 二分无法到达 n-1 的最小 lower，那么减一后，就是可以到达 n-1 的最大 lower
        return bisect_left(range(max_wt + 1), True, key=check) - 1

