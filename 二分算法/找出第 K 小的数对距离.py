'''
转化
第 k 小/大问题的通用转化方法：

第 k 小等价于：求最小的 x，满足绝对差 ≤x 的数对至少有 k 个。（注意是至少不是恰好）
第 k 大等价于：求最大的 x，满足绝对差 ≥x 的数对至少有 k 个。
对于本题，x 越大，越能找到 k 个数对；x 越小，越不能找到 k 个数对。据此，可以二分猜答案。关于二分算法的原理，请看 二分查找 红蓝染色法【基础算法精讲 04】。

现在本题转化成一个判定性问题：

给定整数 mx，统计绝对差 ≤mx 的数对个数 cnt，判断是否满足 cnt≥k。
如何高效统计 cnt 呢？

同向双指针
为方便计算，把 nums 从小到大排序。

排序后，nums[j] 越大，那么满足 i<j 且 nums[j]−nums[i]≤mx 的最小的 i 也越大，我们可以用同向双指针解决这个问题。外层循环枚举 nums[j]，内层循环若 i 不满足上式，就把 i 加一。

内层循环结束后，下标对 (i,j) 是满足要求的。由于 i 越大越能满足要求，所以除了 (i,j)，还有 (i+1,j),(i+2,j),…,(j−1,j) 都是满足要求的。也就是说，当 j 固定时，i,i+1,i+2,…,j−1 都是满足要求的，这一共有 j−i 个，加到 cnt 中。

细节
下面代码采用开区间二分，这仅仅是二分的一种写法，使用闭区间或者半闭半开区间都是可以的，喜欢哪种写法就用哪种。

开区间左端点初始值：−1。绝对差不能是负数，也就是有 0 个数对 ≤−1，由于 0<k，所以无法满足要求。
开区间右端点初始值：排序后的 nums[n−1]−nums[0]。所有数对都满足要求，这有  
2
n(n−1)
​
  个，由于  
2
n(n−1)
​
 ≥k，所以一定满足要求。
对于开区间写法，简单来说 check(mid) == true 时更新的是谁，最后就返回谁。相比其他二分写法，开区间写法不需要思考加一减一等细节，更简单。推荐使用开区间写二分。

答疑
问：为什么二分结束后，答案 ans 一定是 nums 中的某两个数的绝对差？

答：反证法。假设 ans 不是某两个数的绝对差，这意味着第 k 小的绝对差比 ans 小，或者说 ≤ans−1。换句话说，≤ans−1 的数对有 k 个，即 check(ans−1)=true。但根据循环不变量，二分结束后 check(ans−1)=false，矛盾。故原命题成立。


'''
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def check(mx: int) -> bool:
            cnt = i = 0
            for j, x in enumerate(nums):
                while x - nums[i] > mx:
                    i += 1
                cnt += j - i
            return cnt >= k

        left, right = -1, nums[-1] - nums[0]
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right
