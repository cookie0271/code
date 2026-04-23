'''
把二分中点 mid 记作 mx，我们可以贪心地计算要划分出的段数：

初始化段数 cnt=1（第一段），当前这一段的元素和 s=0。
遍历 nums。
如果 s+nums[i]≤mx，则把 nums[i] 加到 s 中。否则我们必须新划分出一段，把 cnt 加一，s 替换成 nums[i]。如果在 cnt 加一之前有 cnt=k，则说明我们划分了超过 k 段，返回 false，表示不满足要求。
遍历结束，返回 true，表示满足要求。
细节
下面代码采用开区间二分，这仅仅是二分的一种写法，使用闭区间或者半闭半开区间都是可以的。

设 nums 的元素和为 S。

开区间左端点初始值：max(nums)−1。元素和不可能比数组最大值还小，一定不满足要求。
开区间右端点初始值：S。无需分割，一定满足要求。

问：如何保证二分结果一定对应着一个划分成 k 段的方案？

答：把二分结果代入 check 函数，可以得到一个划分成 ≤k 段的方案。在此基础上，可以得到划分成 k 段的方案。比如划分成 k−1 段，那么把其中的一个长度至少为 2 的段分成两段，这两段的元素和都比原来的一段小，也满足题目要求，这样就得到了一个划分成 k 段的方案。换句话说，题目其实相当于：把数组划分成至多 k 段。

问：设二分算出来的答案为 ans，如何保证至少有一个子数组的元素和恰好等于 ans？

答：用反证法证明。假设所有子数组的元素和都小于 ans，也就是小于等于 ans−1。这意味着 check(ans−1)=true，但是二分结束后必定有 check(ans−1)=false，矛盾，所以至少有一个子数组的元素和恰好等于 ans。

'''
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx: int) -> bool:
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= mx:
                    s += x
                    continue
                if cnt == k:  # 不能继续划分
                    return False
                cnt += 1  # 新划分一段
                s = x
            return True

        left = max(nums) - 1
        right = sum(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

