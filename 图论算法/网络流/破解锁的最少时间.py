class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        n = len(strength)
        ans = inf
        done = [False] * n
        def dfs(i: int, time: int) -> None:
            nonlocal ans
            # 最优性剪枝：答案不可能变小
            if time >= ans:
                return
            if i == n:
                ans = time
                return
            x = 1 + i * k
            for j, s in enumerate(strength):
                if not done[j]:
                    done[j] = True  # 已开锁
                    dfs(i + 1, time + (s - 1) // x + 1)
                    done[j] = False  # 恢复现场
        dfs(0, 0)
        return ans

