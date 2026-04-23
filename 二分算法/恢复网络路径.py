'''
转化
「最大化最小值」是二分答案的代名词，为什么？

设有效路径上的边权都大于等于下界 lower。

如果下界等于 lower 时，存在有效路径，那么当下界小于 lower 时，约束更加宽松，更加存在有效路径。
如果下界等于 lower 时，不存在有效路径，那么当下界大于 lower 时，约束更加苛刻，更不存在有效路径。
据此，可以二分猜答案。关于二分算法的原理，请看 二分查找 红蓝染色法【基础算法精讲 04】。

现在问题转化成一个判定性问题：

给定下界 lower，能否找到一条有效路径，除了满足题目的两个要求，还满足路径上的边权都大于等于下界 lower。
如果存在有效路径，说明答案 ≥lower，否则答案 <lower。

思路
由于题目保证图是一个 DAG（有向无环图），计算 DP 无后效性，可以用 DAG DP 解决。

定义 dfs(x) 表示从 x 到 n−1 的有效路径的总恢复成本的最小值，即 x 到 n−1 的最短路长度。

枚举 x 的邻居 y，如果 y 在线且边权 wt≥lower，那么问题变成从 y 到 n−1 的有效路径的总恢复成本的最小值，即 dfs(y)，加上边权 wt，更新 dfs(x) 的最小值，即

dfs(x)= 
y
min
​
 dfs(y)+wt
递归边界：dfs(n−1)=0。

递归入口：dfs(0)。

注：也可以用 Dijkstra 算法解决，但那样做时间复杂度要多乘以一个 logm，可能会超时。

细节
1)
下面代码采用开区间二分，这仅仅是二分的一种写法，使用闭区间或者半闭半开区间都是可以的，喜欢哪种写法就用哪种。

开区间左端点初始值：−1。人为规定 −1 一定满足要求。如果二分结果为 −1，那么返回 −1。
开区间右端点初始值：边权的最大值加一。一定不满足要求。注意本题 n≥2，至少要走一条边。
开区间右端点初始值（优化）：0 的出边边权的最大值加一。此时无法从 0 走出去，一定不满足要求。
对于开区间写法，简单来说 check(mid) == true 时更新的是谁，最后就返回谁。相比其他二分写法，开区间写法不需要思考加一减一等细节，更简单。推荐使用开区间写二分。

2)
建图的时候，如果两端点都在线才连边。这样可以减少图的边数，也无需在 DP 过程中判断节点是否在线。

答疑
问：如果答案不等于 −1，为什么二分结束后，答案 ans 一定等于某条边的边权？

答：反证法。假设 ans 不等于某条边的边权，这意味着下界加一后，仍然存在有效路径。换句话说，check(ans+1)=true。但根据循环不变量，二分结束后 check(ans+1)=false，矛盾。故原命题成立。


'''
class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        max_wt = -1
        for x, y, wt in edges:
            if online[x] and online[y]:
                g[x].append((y, wt))
                if x == 0:
                    max_wt = max(max_wt, wt)

        def check(lower: int) -> bool:
            @cache
            def dfs(x: int) -> int:
                if x == n - 1:  # 到达终点
                    return 0
                res = inf
                for y, wt in g[x]:
                    if wt >= lower:
                        res = min(res, dfs(y) + wt)
                return res
            return dfs(0) <= k

        left, right = -1, max_wt + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

'''
写法二：拓扑排序
拓扑排序相当于记忆化搜索的 1:1 翻译版本。严格地翻译需要把每条边反向，再跑拓扑排序。

但也可以从起点开始正着计算，即刷表法。需要注意的是，为了能让我们在拓扑排序中，把入度为 0 的点入队，在拓扑排序之前，先清理那些无法到达的边。比如在有 0→1 的情况下，需要去掉 2→1 这种无法到达的边。


'''
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

