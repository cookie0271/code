class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        n = len(word)
        if n < k:  # 无法满足要求
            return 0

        MOD = 1_000_000_007
        cnts = []
        ans = 1
        cnt = 0
        for i in range(n):
            cnt += 1
            if i == n - 1 or word[i] != word[i + 1]:
                # 如果 cnt = 1，这组字符串必选，无需参与计算
                if cnt > 1:
                    if k > 0:  # 保证空间复杂度为 O(k)
                        cnts.append(cnt - 1)
                    ans = ans * cnt % MOD
                k -= 1  # 注意这里把 k 减小了
                cnt = 0

        if k <= 0:
            return ans

        f = [1] * k
        for c in cnts:
            # 原地计算 f 的前缀和
            for j in range(1, k):
                f[j] = (f[j] + f[j - 1]) % MOD
            # 计算子数组和
            for j in range(k - 1, c, -1):
                f[j] -= f[j - c - 1]
        return (ans - f[-1]) % MOD

