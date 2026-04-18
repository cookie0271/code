class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        a = Counter(s).most_common()  # 按出现次数从大到小排序
        m = a[0][1]
        if m > n - m + 1:
            return ""

        ans = [''] * n
        i = 0
        for ch, cnt in a:
            for _ in range(cnt):
                ans[i] = ch
                i += 2
                if i >= n:
                    i = 1  # 填完偶数填奇数
        return ''.join(ans)

