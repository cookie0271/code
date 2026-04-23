'''
方法一：排序 + 二分查找
把 arr 从小到大排序，这样我们可以二分查找。

遍历 arr ，设 x=arr [i]。我们要判断在 arr 中是否存在元素，在闭区间 [x−d,x+d] 中。考虑 [x−d,x+d] 中的第一个数（最左边的数），也就是在 arr 中二分查找 ≥x−d 的最小的数 y。如果 y 不存在，或者 y>x+d，则说明没有在 [x−d,x+d] 中的元素，符合题目要求，把答案加一。

'''
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for x in arr1:
            i = bisect_left(arr2, x - d)
            if i == len(arr2) or arr2[i] > x + d:
                ans += 1
        return ans
