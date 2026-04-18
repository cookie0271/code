class Solution:
    def smallestNumber(self, pattern: str) -> str:
        i, cur, n = 0, 1, len(pattern)
        ans = [''] * (n + 1)
        while i < n:
            if i and pattern[i] == 'I':
                i += 1
            while i < n and pattern[i] == 'I':
                ans[i] = digits[cur]
                cur += 1
                i += 1
            i0 = i
            while i < n and pattern[i] == 'D':
                i += 1
            for j in range(i, i0 - 1, -1):
                ans[j] = digits[cur]
                cur += 1
        return ''.join(ans)

