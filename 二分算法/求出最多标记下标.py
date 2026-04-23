'''
方法一：二分答案
提示 1
如果 2⋅nums[i]≤nums[j]，则称 nums[i] 与 nums[j] 匹配。

如果可以匹配 k 对，那么也可以匹配小于 k 对，去掉一些数对即可做到。

如果无法匹配 k 对，那么也无法匹配大于 k 对（反证法）。

所以 k 越大，越无法选出 k 个能匹配的数对。有单调性，就可以二分答案。二分算法的理论讲解见【基础算法精讲 04】。

提示 2
现在问题变成：

能否从 nums 中选出 k 个能匹配的数对？
要让哪些数匹配呢？

结论：从小到大排序后，如果存在 k 对匹配，那么一定可以让最小的 k 个数与最大的 k 个数匹配。

证明：假设不是最小的 k 个数与最大的 k 个数匹配，那么我们总是可以把 nums[i] 替换成比它小的且不在匹配中的数，这仍然是匹配的；同理，把 nums[j] 替换成比它大的且不在匹配中的数，这仍然是匹配的。所以如果存在 k 对匹配，那么一定可以让最小的 k 个数和最大的 k 个数匹配。

反过来说，如果最小的 k 个数无法和最大的 k 个数匹配，则任意 k 对都无法匹配。（也可以用反证法证明）

从小到大排序后，nums[0] 要与 nums[n−k] 匹配。如果不这样做，nums[0] 与在 nums[n−k] 右侧的数匹配，相当于占了一个位置，那么后续要选个更大的 nums[i] 与 nums[n−k] 匹配，这不一定能匹配得上。

一般地，nums[i] 要与 nums[n−k+i] 匹配。

如果对于所有的 0≤i<k，都满足 2⋅nums[i]≤nums[n−k+i]，那么就可以从 nums 中选出 k 个能匹配的数对。

细节
下面代码采用开区间二分，这仅仅是二分的一种写法，使用闭区间或者半闭半开区间都是可以的。

开区间左端点初始值：0。无论 nums 是什么样，一定能选出 0 个匹配。
开区间右端点初始值：⌊ 
2
n
​
 ⌋+1。最多能选 ⌊ 
2
n
​
 ⌋ 个匹配，再多一个就不行了。
对于开区间写法，简单来说 check(mid) == true 时更新的是谁，最后就返回谁。相比其他二分写法，开区间写法不需要思考加一减一等细节，更简单。推荐使用开区间写二分。

'''
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums) // 2 + 1  # 开区间
        while left + 1 < right:
            k = (left + right) // 2
            if all(nums[i] * 2 <= nums[i - k] for i in range(k)):
                left = k
            else:
                right = k
        return left * 2  # 最多匹配 left 对，有 left * 2 个数

'''
方法二：同向双指针
由方法一的匹配方式可知，我们需要用 nums 左半部分中的数，去匹配 nums 右半部分中的数。

在 nums 的右半部分中，找到第一个满足 2⋅nums[0]≤nums[j] 的 j，那么 nums[1] 只能匹配右半部分中的下标大于 j 的数，依此类推。

这可以用同向双指针实现。

'''
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        for x in nums[(len(nums) + 1) // 2:]:
            if nums[i] * 2 <= x:  # 找到一个匹配
                i += 1
        return i * 2

