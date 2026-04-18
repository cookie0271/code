class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        for x in range(1, target[-1] + 1):
            ans.append("Push")  # 先把 x 入栈（题目要求）
            if x == target[i]:  # x 是我们要的数
                i += 1
            else:  # x 不是我们要的数，出栈
                ans.append("Pop")
        return ans

