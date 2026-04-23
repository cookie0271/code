'''
方法一：二分间接值
由于正方形边长越大，越不合法，有单调性，所以可以二分边长的一半。

在二分中统计遇到的字符，如果没有遇到重复的字符，说明正方形合法，用字符个数更新答案的最大值。

关于二分算法的原理，请看 二分查找 红蓝染色法【基础算法精讲 04】

代码用到了一些位运算技巧，原理请看 从集合论到位运算，常见位运算技巧分类总结！

答疑
问：为什么可以直接更新 ans，为什么不需要写 ans = max(ans, ...)？

答：更新 ans 时必然会伴随着二分区间左边界 left 的更新，那么下一次更新 ans 的时候，正方形的边长一定更长，包含的点数不会变少，所以可以直接更新，无需写 max。


'''
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        ans = 0
        def check(size: int) -> bool:
            vis = set()
            for (x, y), c in zip(points, s):
                if abs(x) <= size and abs(y) <= size:  # 点在正方形中
                    if c in vis:
                        return True
                    vis.add(c)
            nonlocal ans
            ans = len(vis)
            return False
        # 注意 range 并不会创建 list，它是 O(1) 的
        bisect_left(range(1_000_000_001), True, key=check)
        return ans

