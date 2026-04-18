class Solution:
    def f(self, word: str, k: int) -> int:
        cnt1 = defaultdict(int)  # 每种元音的个数
        ans = cnt2 = left = 0  # cnt2 维护辅音个数
        for b in word:
            if b in "aeiou":
                cnt1[b] += 1
            else:
                cnt2 += 1
            while len(cnt1) == 5 and cnt2 >= k:
                out = word[left]
                if out in "aeiou":
                    cnt1[out] -= 1
                    if cnt1[out] == 0:
                        del cnt1[out]
                else:
                    cnt2 -= 1
                left += 1
            ans += left
        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.f(word, k) - self.f(word, k + 1)

