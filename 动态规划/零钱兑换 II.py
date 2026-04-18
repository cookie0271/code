class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, c: int) -> int:
            if i < 0:
                return 1 if c == 0 else 0
            if c < coins[i]:  # 只能不选
                return dfs(i - 1, c)
            # 不选 + 继续选
            return dfs(i - 1, c) + dfs(i, c - coins[i])

        return dfs(len(coins) - 1, amount)

