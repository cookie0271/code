class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        ans = inf
        for i in range(n - 2):
            x = nums[i]
            # 优化
            if i and x == nums[i - 1]:
                continue  

            # 优化
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三数之和不会比 s 还小
                if s - target < abs(ans - target):
                    ans = s
                break

            # 优化
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < abs(ans - target):
                    ans = s
                continue

            # 双指针
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return target
                if abs(s - target) < abs(ans - target):  # s 离 target 更近
                    ans = s
                if s > target:
                    k -= 1
                else:  # s < target
                    j += 1
        return ans

