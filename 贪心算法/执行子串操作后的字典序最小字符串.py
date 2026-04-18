class Solution:
    def smallestString(self, s: str) -> str:
        t = list(s)
        for i, c in enumerate(t):
            if c == 'a':
                continue
            # 继续向后遍历
            for j in range(i, len(t)):
                if t[j] == 'a':
                    break
                t[j] = chr(ord(t[j]) - 1)
            return ''.join(t)
        # 所有字母均为 a
        t[-1] = 'z'
        return ''.join(t)
