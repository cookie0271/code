class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, in_ in enumerate(fruits):
            cnt[in_] += 1  # fruits[right] 进入窗口
            while len(cnt) > 2:  # 不满足要求
                out = fruits[left]
                cnt[out] -= 1  # fruits[left] 离开窗口
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

