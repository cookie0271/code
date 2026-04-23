'''
问：如何理解 end = lowerBound(nums, target + 1) - 1 这段代码？

答：要想找到 ≤target 的最后一个数，无需单独再写一个二分。我们可以先找到这个数的右边相邻数字，也就是 >target 的第一个数。在所有数都是整数的前提下，>target 等价于 ≥target+1，这样就可以复用我们已经写好的二分函数了，即 lowerBound(nums, target + 1)，算出这个数的下标后，将其减一，就得到 ≤target 的最后一个数的下标。

问：如果 ≥target+1 的第一个数不存在怎么办？

答：这说明数组中的数都 ≤target。如果数组中有 target，那么数组的最后一个数（下标 n−1）就是 target（因为数组是递增的）。同时，lowerBound(nums, target + 1) 在这种情况下会返回 n，减一得到 n−1，这正是我们要计算的下标。

问：为什么要写 left + (right - left) / 2？

答：在面试或者实际场景中，你不一定知道输入的数组有多长，万一数组长度达到 int 最大值，left + right 可能会发生加法溢出。当然，如果只看本题的数据范围，写 (left + right) / 2 也可以。对于 Python 来说，由于没有溢出这个概念，所以可以直接相加。

问：怎么判断我写的是哪一种二分？

答：看 while 循环的条件，如果是 left <= right，就是闭区间；如果是 left < right，就是半闭半开区间；如果是 left + 1 < right，就是开区间。

问：对于闭区间写法，为什么 nums[mid] >= target 的时候要写 right = mid - 1？此时的 mid 不是有可能是答案吗？这样写不会错过答案吗？

答：答案在区间外面，不在区间里面。如果觉得答案在区间里面的话，请思考这个问题：闭区间循环结束后 left>right，区间 [left,right] 是空的，什么也没有，难道答案在空区间里面吗？

问：我看到一种二分的写法，在二分的过程中，额外记录答案的值，你对此怎么看？

答：喜欢这种写法的同学，推荐写开区间二分，因为开区间二分 if 条件成立时更新的是哪个变量，最后返回的也就是哪个变量。这和记录答案的做法如出一辙。

问：关于开区间二分，如何理解 −1 和 n 这两个下标？

答：可以假设 nums[−1]=−∞ 以及 nums[n]=∞，此时 nums 仍然是有序的。在这种情况下，nums[−1]<target，所以 −1 是红色；nums[n]≥target，所以 n 是蓝色。这个思想可以推广到二分答案，见本文末尾的二分题单。

'''
class Solution:
    # lower_bound 返回最小的满足 nums[i] >= target 的下标 i
    # 如果数组为空，或者所有数都 < target，则返回 len(nums)
    # 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
    def lower_bound(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1  # 闭区间 [left, right]
        while left <= right:  # 区间不为空
            # 循环不变量：
            # nums[left-1] < target
            # nums[right+1] >= target
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1  # 范围缩小到 [left, mid-1]
            else:
                left = mid + 1  # 范围缩小到 [mid+1, right]
        # 循环结束后 left = right+1
        # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
        # 所以 left 就是第一个 >= target 的元素下标
        return left

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.lower_bound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]  # nums 中没有 target
        # 如果 start 存在，那么 end 必定存在
        end = self.lower_bound(nums, target + 1) - 1
        return [start, end]

