class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mx: int) -> bool:
            cnt = 0  # matrix 中的 <= mx 的元素个数
            i, j = 0, n - 1  # 从右上角开始
            while i < n and j >= 0 and cnt < k:
                if matrix[i][j] > mx:
                    j -= 1  # 排除第 j 列
                else:
                    cnt += j + 1  # 从 matrix[i][0] 到 matrix[i][j] 都 <= mx
                    i += 1
            return cnt >= k

        left, right = matrix[0][0] - 1, matrix[-1][-1]
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right

