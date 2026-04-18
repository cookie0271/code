class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        mark = [0] * (k + 1)  # mark[v] 标记 v 属于哪个子段
        ans, left = 1, k
        for v in rolls:
            if mark[v] < ans:
                mark[v] = ans
                left -= 1
                if left == 0:
                    left = k
                    ans += 1
        return ans

