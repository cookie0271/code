'''
第 k 小/大问题的通用转化方法：

第 k 小等价于：求最小的 x，满足 ≤x 的数至少有 k 个。（注意是至少不是恰好）
第 k 大等价于：求最大的 x，满足 ≥x 的数至少有 k 个。
对于本题，x 越大，越能找到 k 个数；x 越小，越不能找到 k 个数。据此，可以二分猜答案。关于二分算法的原理，请看 二分查找 红蓝染色法【基础算法精讲 04】。

现在本题转化成一个判定性问题：

给定整数 x，统计乘法表中 ≤x 的元素个数 cnt，判断是否满足 cnt≥k。
从第 1 行到第 m 行，我们一行一行地遍历乘法表。

细节
如果写闭区间二分，左右边界是 [1,mn−1]，注意 mn 不需要在二分区间内，因为如果我们没有在 [1,mn−1] 中找到答案，那么答案就一定是 mn。

下面代码用的是开区间，即 (0,mn)。

开区间左端点 0 一定不满足要求：≤0 的数有 0<k 个。
开区间右端点 mn 一定满足要求：≤mn 的数有 mn≥k 个。
答疑
问：为什么二分结束后，答案 ans 一定在乘法表中？

答：反证法。假设 ans 不在乘法表中，这意味着乘法表中第 k 小的数比 ans 小，或者说 ≤ans−1。换句话说，≤ans−1 的数有 k 个，即 check(ans−1)=true。但根据循环不变量，二分结束后 check(ans−1)=false，矛盾。故原命题成立。


'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def check(x: int) -> bool:
            cnt = 0
            for i in range(1, m + 1):
                cnt += min(x // i, n)
            return cnt >= k

        left, right = 0, m * n
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

