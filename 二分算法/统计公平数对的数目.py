'''
方法一：二分查找
由于排序不影响答案，可以先（从小到大）排序，这样可以二分查找。

nums 是 [1,2] 还是 [2,1]，算出来的答案是一样的，因为加法满足交换律 a+b=b+a。

排序后，枚举右边的 nums[j]，那么左边的 nums[i] 需要满足 0≤i<j 以及

lower−nums[j]≤nums[i]≤upper−nums[j]
计算 ≤upper−nums[j] 的元素个数，减去 <lower−nums[j] 的元素个数，即为满足上式的元素个数。（联想一下前缀和）

由于 nums 是有序的，我们可以在 [0,j−1] 中二分查找，原理见【基础算法精讲 04】：

找到 >upper−nums[j] 的第一个数，设其下标为 r，那么下标在 [0,r−1] 中的数都是 ≤upper−nums[j] 的，这有 r 个。如果 [0,j−1] 中没有找到这样的数，那么二分结果为 j。这意味着 [0,j−1] 中的数都是 ≤upper−nums[j] 的，这有 j 个。
找到 ≥lower−nums[j] 的第一个数，设其下标为 l，那么下标在 [0,l−1] 中的数都是 <lower−nums[j] 的，这有 l 个。如果 [0,j−1] 中没有找到这样的数，那么二分结果为 j。这意味着 [0,j−1] 中的数都是 <lower−nums[j] 的，这有 j 个。
满足 lower−nums[j]≤nums[i]≤upper−nums[j] 的 nums[i] 的个数为 r−l，加入答案。


'''
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for j, x in enumerate(nums):
            # 注意要在 [0, j-1] 中二分，因为题目要求两个下标 i < j
            r = bisect_right(nums, upper - x, 0, j)
            l = bisect_left(nums, lower - x, 0, j)
            ans += r - l  
        return ans

'''
方法二：相向三指针
由于随着 nums[j] 的变大，upper−nums[j] 和 lower−nums[j] 都在变小，有单调性，可以用相向三指针 j,l,r 代替方法一中的二分查找：

初始化 l=r=n。
从左到右遍历（排序后的）nums。
找 >upper−nums[j] 的第一个数：如果 nums[r−1]>upper−nums[j]，说明 r 太大了，可以继续减小。循环结束后的 r，与 j 取最小值后，就是方法一的二分查找计算出的 r。
找 ≥lower−nums[j] 的第一个数：如果 nums[l−1]≥lower−nums[j]，说明 l 太大了，可以继续减小。循环结束后的 l，与 j 取最小值后，就是方法一的二分查找计算出的 l。

'''
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        l = r = len(nums)
        for j, x in enumerate(nums):
            while r and nums[r - 1] > upper - x:
                r -= 1
            while l and nums[l - 1] >= lower - x:
                l -= 1
            # 在方法一中，二分的结果必须 <= j
            # 方法二同理，要保证 l 和 r 都 <= j
            ans += min(r, j) - min(l, j)
        return ans

'''
方法三：两次相向双指针
写法一
我们也可以枚举左边的 i，统计右边有多少个合法的 j。

枚举 i，计算满足 j>i 且 nums[j]≤upper−nums[i] 的 j 的个数，记作 count(upper)。

枚举 i，计算满足 j>i 且 nums[j]<lower−nums[i]，也就是 nums[j]≤lower−1−nums[i] 的 j 的个数，记作 count(lower−1)。

答案就是 count(upper)−count(lower−1)。

怎么计算 count(upper)？

初始化 j=n−1。枚举 i，如果 nums[j]>upper−nums[i]，就减小 j，直到 j=i 或者 nums[j]≤upper−nums[i] 为止。

如果 j=i，那么继续循环也无法满足 j>i 的要求，直接退出循环。

由于数组是有序的，如果 nums[i]+nums[j]≤upper，那么对于更小的 j，也同样满足这个不等式。所以 [i+1,j] 范围内的下标都可以是 j，这有 j−i 个，加入答案。


'''
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def count(upper: int) -> int:
            res = 0
            j = len(nums) - 1
            for i, x in enumerate(nums):
                while j > i and nums[j] > upper - x:
                    j -= 1
                if j == i:
                    break
                res += j - i
            return res
        return count(upper) - count(lower - 1)

'''
写法二
初始化 i=0，j=n−1。

如果 nums[i]+nums[j]≤upper，那么对于更小的 j，也同样满足这个不等式。所以 [i+1,j] 范围内的下标 j 都可以和 i 配对，这有 j−i 个，加入答案，然后把 i 加一。

如果 nums[i]+nums[j]>upper，那么对于更大的 i，也同样不满足题目要求。所以 [i,j−1] 范围内的下标 i 都无法与 j 配对，直接把 j 减一。


'''
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        def count(upper: int) -> int:
            res = 0
            i, j = 0, len(nums) - 1
            while i < j:
                if nums[i] + nums[j] <= upper:
                    res += j - i
                    i += 1
                else:
                    j -= 1
            return res
        return count(upper) - count(lower - 1)
