class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, n = 0, len(s)
        for j, c in enumerate(t):
            while i < n and s[i] != t[j]: i += 1
            if i == n: return len(t) - j
            i += 1
        return 0

