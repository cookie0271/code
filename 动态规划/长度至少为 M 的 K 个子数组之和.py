class Solution:
    def maxSum(self, nums: List[int], k: int, m: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))  # nums 的前缀和
        f = [[0] * (n + 1) for _ in range(k + 1)]
        for i in range(1, k + 1):
            f[i][i * m - 1] = mx = -inf
            # 左右两边留出足够空间给其他子数组
            for j in range(i * m, n - (k - i) * m + 1):
                # mx 表示最大的 f[i-1][L]-s[L]，其中 L 在区间 [(i-1)*m, j-m] 中
                mx = max(mx, f[i - 1][j - m] - s[j - m])
                f[i][j] = max(f[i][j - 1], mx + s[j])  # 不选 vs 选
        return f[k][n]

