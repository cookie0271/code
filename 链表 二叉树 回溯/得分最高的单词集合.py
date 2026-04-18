class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ans = 0
        left = Counter(letters)
        score = dict(zip(ascii_lowercase, score))  # 字母对应的分数

        def dfs(i: int, total: int) -> None:
            if i < 0:  # base case
                nonlocal ans
                ans = max(ans, total)
                return

            # 不选 words[i]
            dfs(i - 1, total)

            # 选 words[i]
            for j, c in enumerate(words[i]):
                if left[c] == 0:  # 剩余字母不足
                    for c in words[i][:j]:  # 撤销
                        left[c] += 1
                    return
                left[c] -= 1  # 减少剩余字母
                total += score[c]  # 累加得分

            dfs(i - 1, total)

            # 恢复现场
            for c in words[i]:
                left[c] += 1

        dfs(len(words) - 1, 0)
        return ans

