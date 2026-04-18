class Solution:
    def partitionString(self, s: str) -> List[str]:
        ans = []
        cur = root = {}
        left = 0
        for i, c in enumerate(s):
            if c not in cur:  # 无路可走？
                cur[c] = {}  # 那就造路！
                ans.append(s[left: i + 1])
                left = i + 1
                cur = root  # 重置
            else:
                cur = cur[c]
        return ans

