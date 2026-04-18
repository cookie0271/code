class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # 判断 s 是否为 t 的子序列
        def is_subseq(s: str, t: str) -> bool:
            i = 0
            for c in t:
                if s[i] == c:
                    i += 1
                    if i == len(s):  # 所有字符匹配完毕
                        return True  # s 是 t 的子序列
            return False

        ans = -1
        for i, s in enumerate(strs):
            if len(s) > ans and \
               all(j == i or not is_subseq(s, t) for j, t in enumerate(strs)):
                ans = len(s)
        return ans

