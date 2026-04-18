class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                stacks[ord(c) - ord('a')].append(i)
                continue
            for st in stacks:
                if st:
                    s[st.pop()] = '*'
                    break
        return ''.join(c for c in s if c != '*')

