'''
考虑这样一个问题：

能否让每个小孩都至少有 low 颗糖果？
low 越大，越难实现；low 越小，越容易实现。有这样的性质，就可以二分猜答案了。关于二分算法，请看 二分查找 红蓝染色法【基础算法精讲 04】。

比如最终 low=5 可以满足要求，但 low=6 无法满足要求，那么答案就是 5。

由于糖果堆只能分割不能合并，对于 candies[i] 来说，可以分出

c=⌊ 
low
candies[i]
​
 ⌋
个大小为 low 的糖果堆，满足 c 个小孩。


细节
下面代码采用开区间二分，这仅仅是二分的一种写法，使用闭区间或者半闭半开区间都是可以的。

开区间左端点初始值：0。不分配糖果就能满足要求。
开区间右端点初始值：max(candies)+1。糖果堆只能分割不能合并，一定无法满足要求。


'''
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(low: int) -> bool:
            return sum(c // low for c in candies) >= k

        left, right = 0, min(max(candies), sum(candies) // k) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

