class Solution:
    def maxSubstrings(self, word: str) -> int:
        ans = 0
        pos = {}
        for i, ch in enumerate(word):
            if ch not in pos:  # 之前没有遇到
                pos[ch] = i
            elif i - pos[ch] > 2:  # 再次遇到，且子串长度 >= 4
                ans += 1
                # 找下一个子串
                pos.clear()
        return ans

