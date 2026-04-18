class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = [0] * (max(arrivals) + 1)  # 或者用 defaultdict(int)
        ans = 0
        for i, x in enumerate(arrivals):
            # x 进入窗口
            if cnt[x] == m:  # x 的个数已达上限
                # 注意 x 在未来要离开窗口，但由于已经丢弃，不能在离开窗口时修改 cnt
                # 这里直接置为 0，未来离开窗口就是 cnt[0]--，不影响答案
                arrivals[i] = 0  # 丢弃 arrivals[i]
                ans += 1
            else:
                cnt[x] += 1

            # 左端点元素离开窗口，为下一个循环做准备
            left = i + 1 - w
            if left >= 0:
                cnt[arrivals[left]] -= 1
        return ans

