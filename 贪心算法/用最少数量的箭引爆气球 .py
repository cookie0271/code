class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])  # 按照右端点从小到大排序
        ans = 0
        pre = -inf
        for start, end in points:
            if start > pre:  # 上一个点在区间左边
                ans += 1
                pre = end  # 在区间的最右边放一个点
        return ans

