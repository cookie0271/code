'''
思路
假设除数为 m。

根据题意，每个数除以 m 再上取整，元素和为

i=0
∑
n−1
​
 ⌈ 
m
nums[i]
​
 ⌉
由于 m 越大，上式越小，有单调性，可以二分答案。关于二分的原理，请看视频【基础算法精讲 04】。

最小的满足  
i=0
∑
n−1
​
 ⌈ 
m
nums[i]
​
 ⌉≤threshold 的 m 就是答案。

细节
1)
下面代码采用开区间二分，这仅仅是二分的一种写法，使用闭区间或者半闭半开区间都是可以的。

开区间左端点初始值：0。一定不满足题目要求。
开区间右端点初始值：max(nums)。此时  
i=0
∑
n−1
​
 ⌈ 
m
nums[i]
​
 ⌉=n≤threshold 一定成立。（注意题目数据范围保证 n≤threshold）
如果你喜欢用闭区间，左右端点可以分别初始化成 1 和 max(nums)−1。

在练习时，请注意「求最小」和「求最大」的二分写法上的区别。

「求最小」和二分查找求「排序数组中某元素的第一个位置」是类似的，按照红蓝染色法，左边是不满足要求的（红色），右边则是满足要求的（蓝色）。

「求最大」的题目则相反，左边是满足要求的（蓝色），右边是不满足要求的（红色）。这会导致二分写法和上面的「求最小」有一些区别。

以开区间二分为例：

求最小：check(mid) == true 时更新 right = mid，反之更新 left = mid，最后返回 right。
求最大：check(mid) == true 时更新 left = mid，反之更新 right = mid，最后返回 left。
对于开区间写法，简单来说 check(mid) == true 时更新的是谁，最后就返回谁。相比其他二分写法，开区间写法不需要思考加一减一等细节，个人推荐使用开区间写二分。


'''
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if sum((x - 1) // mid for x in nums) <= threshold - len(nums):
                right = mid
            else:
                left = mid
        return right

