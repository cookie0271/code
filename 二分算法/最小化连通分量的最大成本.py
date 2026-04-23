'''
如果 k=n，无需合并，返回 0。

否则，为了最小化答案，我们可以用并查集从小到大合并，直到连通块个数等于 k 为止。此时，合并边之前有 k+1 个连通块，合并后有 k 个连通块，且参与合并的边权都是尽量小的，返回当前边的边权。合并更大的边权是没有意义的，因为小于等于最大边权的边我们都能合并，合并更大边权不会得到更优解。


'''
# 完整的并查集模板，见我的数据结构题单
class UnionFind:
    def __init__(self, n: int):
        # 一开始有 n 个集合 {0}, {1}, ..., {n-1}
        # 集合 i 的代表元是自己，大小为 1
        self._fa = list(range(n))  # 代表元
        self.cc = n  # 连通块个数

    # 返回 x 所在集合的代表元
    # 同时做路径压缩，也就是把 x 所在集合中的所有元素的 fa 都改成代表元
    def find(self, x: int) -> int:
        # 如果 fa[x] == x，则表示 x 是代表元
        if self._fa[x] != x:
            self._fa[x] = self.find(self._fa[x])  # fa 改成代表元
        return self._fa[x]

    # 把 from 所在集合合并到 to 所在集合中
    def merge(self, from_: int, to: int) -> None:
        x, y = self.find(from_), self.find(to)
        if x == y:  # from 和 to 在同一个集合，不做合并
            return
        self._fa[x] = y  # 合并集合。修改后就可以认为 from 和 to 在同一个集合了
        self.cc -= 1  # 成功合并，连通块个数减一


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k == n:
            return 0
    
        edges.sort(key=lambda e: e[2])
        u = UnionFind(n)
        for x, y, w in edges:
            u.merge(x, y)
            if u.cc == k:
                return w

