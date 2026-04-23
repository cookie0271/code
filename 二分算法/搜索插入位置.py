'''
问：为什么不在二分的过程中，找到 target 就立刻返回？

答：这种写法适用范围很窄。在有多个等于 target 的数的情况下，如果在二分的过程中立刻返回，我们得到的可能不是第一个等于 target 的数的下标。为什么返回第一个等于 target 的数的下标更好呢？因为这可以解决更复杂的题目，比如给你一个有序数组 [1,1,3,3,3,3,5]，让你计算有多少个数小于 3。我们可以二分查找第一个等于 3 的数的下标 2，那么下标小于 2 的数就是元素值小于 3 的数，这有 2 个。对比可以发现，如果在二分中途就立刻返回，我们不一定找到的是第一个等于 3 的数的下标，所以不一定能算出正确答案 2。

问：为什么代码没有特判所有数都小于 target 的情况？

答：如果所有数都小于 target，那么循环中更新的只有 left，无论下面哪种二分写法，最后都一定会返回数组长度，所以无需特判这种情况。

问：如果所有数都大于 target 呢？

答：代码会返回 0。

问：是否需要特判 nums[mid]=target 的情况？

答：可以，但没必要。

'''
# lower_bound 返回最小的满足 nums[i] >= target 的 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]

# 闭区间写法
def lower_bound(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right]
        else:
            right = mid - 1  # 范围缩小到 [left, mid-1]
    return left

# 左闭右开区间写法
def lower_bound2(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)  # 左闭右开区间 [left, right)
    while left < right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right] >= target
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1  # 范围缩小到 [mid+1, right)
        else:
            right = mid  # 范围缩小到 [left, mid)
    return left  # 或者 right

# 开区间写法
def lower_bound3(nums: List[int], target: int) -> int:
    left, right = -1, len(nums)  # 开区间 (left, right)
    while left + 1 < right:  # 区间不为空
        mid = (left + right) // 2
        # 循环不变量：
        # nums[left] < target
        # nums[right] >= target
        if nums[mid] < target:
            left = mid  # 范围缩小到 (mid, right)
        else:
            right = mid  # 范围缩小到 (left, mid)
    return right

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return lower_bound(nums, target)  # 选择其中一种写法即可

