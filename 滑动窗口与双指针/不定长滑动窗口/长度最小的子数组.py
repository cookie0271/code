class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        s = left = 0
        ans = inf

        for i, x in enumerate(nums):
            # 1. 入
            cnt[x] += 1
            if cnt[x] == 1:
                s += x

            while s >= k:
                # 2. 更新答案
                ans = min(ans, i - left + 1)

                # 3. 出
                out = nums[left]
                cnt[out] -= 1
                if cnt[out] == 0:
                    s -= out
                left += 1

        return ans if ans < inf else -1

