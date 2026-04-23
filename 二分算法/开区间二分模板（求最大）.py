'''
请注意「求最小」和「求最大」在二分写法上的区别。

「求最小」和二分查找求「排序数组中某元素的第一个位置」是类似的，按照红蓝染色法，左边是不满足要求的（红色），右边则是满足要求的（蓝色）。

「求最大」的题目则相反，左边是满足要求的（蓝色），右边是不满足要求的（红色）。这会导致二分写法和上面的「求最小」有一些区别。

以开区间二分为例：

求最小：check(mid) == true 时更新 right = mid，反之更新 left = mid，最后返回 right。
求最大：check(mid) == true 时更新 left = mid，反之更新 right = mid，最后返回 left。
对于开区间写法，简单来说 check(mid) == true 时更新的是谁，最后就返回谁。相比其他二分写法，开区间写法不需要思考加一减一等细节，推荐使用开区间写二分。

'''
class Solution:
    # 计算满足 check(x) == True 的最大整数 x
    def binarySearchMax(self, nums: List[int]) -> int:
        # 二分猜答案：判断 mid 是否满足题目要求
        def check(mid: int) -> bool:
            # TODO

        left =   # 循环不变量：check(left) 恒为 True
        right =   # 循环不变量：check(right) 恒为 False
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid  # 注意这里更新的是 left，和上面的模板反过来
            else:
                right = mid
        # 循环结束后 left+1 = right
        # 此时 check(left) == True 而 check(left+1) == check(right) == False
        # 所以 left 就是最大的满足 check 的值
        return left  # check 更新的是谁，最终就返回谁

