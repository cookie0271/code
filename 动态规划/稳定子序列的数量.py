# 更快的写法见【Python3 写法二】
class Solution:
    def countStableSubsequences(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        f = [[0, 0], [0, 0]]
        for x in nums:
            x %= 2
            f[x][1] = (f[x][1] + f[x][0]) % MOD
            f[x][0] = (f[x][0] + f[x ^ 1][0] + f[x ^ 1][1] + 1) % MOD
        return (f[0][0] + f[0][1] + f[1][0] + f[1][1]) % MOD
