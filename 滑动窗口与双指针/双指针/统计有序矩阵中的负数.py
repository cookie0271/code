class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        i, j = 0, n - 1  # 从右上角开始
        while i < m and j >= 0:  # 还有剩余元素
            if grid[i][j] < 0:
                ans += m - i  # 这一列剩余元素都是负数
                j -= 1
            else:
                i += 1  # 这一行剩余元素全都非负，排除
        return ans
