class Solution:
    def maxSumOfSquares(self, n: int, s: int) -> str:
        if n * 9 < s:
            return ""
        ans = '9' * (s // 9)
        if s % 9:
            ans += digits[s % 9]
        return ans + '0' * (n - len(ans))
