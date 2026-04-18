class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda c: c[1])  # 按照 last_day 从小到大排序
        h = []  # 最大堆
        day = 0  # 已消耗时间
        for duration, last_day in courses:
            if day + duration <= last_day:  # 没有超过 last_day，直接学习
                day += duration
                heappush_max(h, duration)
            elif h and duration < h[0]:  # 该课程的时间比之前的最长时间要短
                # 反悔，撤销之前 duration 最长的课程，改为学习该课程
                # 节省出来的时间，能在后面上完更多的课程
                day -= heapreplace_max(h, duration) - duration
        return len(h)

