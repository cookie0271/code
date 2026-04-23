'''
问：如何把二分答案与数组上的二分查找联系起来？

答：假设答案在区间 [2,5] 中，我们相当于在一个虚拟数组 [check(2),check(3),check(4),check(5)] 中二分找第一个（或者最后一个）值为 true 的 check(x)。这同样可以用红蓝染色法思考。

问：有些题目，明明 m 可以是答案，但却不在初始二分区间中。比如闭区间二分初始化 right=m−1（或者开区间 right=m），这不会算错吗？

答：不会算错。注意「答案所在区间」和「二分区间」是两个概念。想一想，如果二分的 while 循环每次更新的都是 left，那么最终答案是什么？正好就是 m。一般地，如果一开始就能确定 m 一定可以满足题目要求，那么 m 是不需要在二分区间中的。换句话说，二分区间是「尚未确定是否满足题目要求」的数的范围。那些在区间外面的数，都是已确定的满足（不满足）题目要求的数。

问：什么是循环不变量？

答：想一想，对于求最小的题目，开区间二分的写法，为什么最终返回的是 right，而不是别的数？在初始化（循环之前）、循环中、循环结束后，都时时刻刻保证 check(right) == true 和 check(left) == false，这就叫循环不变量。根据循环不变量，循环结束时 left+1=right，那么 right 就是最小的满足要求的数（因为再 −1 就不满足要求了），所以答案是 right。

注：部分题目可以优化二分边界，减少二分次数，从而减少代码运行时间。对于初次接触二分答案的同学，无需强求自己写出最优的代码，设定一个比较大的二分上界也是可以的。


'''
class Solution:
    # 计算满足 check(x) == True 的最小整数 x
    def binarySearchMin(self, nums: List[int]) -> int:
        # 二分猜答案：判断 mid 是否满足题目要求
        def check(mid: int) -> bool:
            # TODO

        left =   # 循环不变量：check(left) 恒为 False
        right =   # 循环不变量：check(right) 恒为 True
        while left + 1 < right:  # 开区间不为空
            mid = (left + right) // 2
            if check(mid):  # 说明 check(>= mid 的数) 均为 True
                right = mid  # 接下来在 (left, mid) 中二分答案
            else:  # 说明 check(<= mid 的数) 均为 False
                left = mid  # 接下来在 (mid, right) 中二分答案
        # 循环结束后 left+1 = right
        # 此时 check(left) == False 而 check(left+1) == check(right) == True
        # 所以 right 就是最小的满足 check 的值
        return right

