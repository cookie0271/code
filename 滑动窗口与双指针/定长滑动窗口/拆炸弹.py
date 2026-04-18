class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        r = k + 1 if k > 0 else n  # 第一个窗口的右开端点
        k = abs(k)
        s = sum(code[r - k: r])  # 第一个窗口的元素和

        ans = [0] * n
        for i in range(n):
            ans[i] = s
            s += code[r % n] - code[(r - k) % n]
            r += 1
        return ans

