class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        f = [1] + [0] * n
        for i in range(1, n + 1):
            v = i ** x
            if v > n:
                break
            for s in range(n, v - 1, -1):
                f[s] += f[s - v]
        return f[n] % 1_000_000_007

