class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda p: p[0])
        h = []
        for left, right in intervals:
            if h and left > h[0]: heapreplace(h, right)
            else: heappush(h, right)
        return len(h)
