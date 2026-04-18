class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda p: p[0])  # 按照左端点从小到大排序
        start, end = 1, 0  # 当前合并区间的左右端点
        for s, e in meetings:
            if s > end:  # 不相交
                days -= end - start + 1  # 当前合并区间的长度
                start = s  # 下一个合并区间的左端点
            end = max(end, e)
        days -= end - start + 1  # 最后一个合并区间的长度
        return days
