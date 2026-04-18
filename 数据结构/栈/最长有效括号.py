class Solution:
    def solve(self, s: Iterable[str], left_ch: str) -> int:
        ans = left = right = 0
        for ch in s:
            if ch == left_ch:
                left += 1
            else:
                right += 1
            if left < right:  # 拆弹器太多了，ch 变成红线，重置计数器
                left = right = 0
            elif left == right:  # 完美拆弹
                ans = max(ans, right * 2)
        return ans

    def longestValidParentheses(self, s: str) -> int:
        return max(self.solve(s, '('), self.solve(reversed(s), ')'))  # reversed 是 O(1) 的

