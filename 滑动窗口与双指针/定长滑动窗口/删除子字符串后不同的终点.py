DIRS = {
    'L': (-1, 0),
    'R': (1, 0),
    'D': (0, -1),
    'U': (0, 1),
}

class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        st = set()
        x = y = 0
        for i, c in enumerate(s):
            # 1. 入
            dx, dy = DIRS[c]
            x += dx
            y += dy

            left = i + 1 - k  # 窗口左端点
            if left < 0:  # 窗口大小不足 k
                continue

            # 2. 记录答案
            st.add((x, y))

            # 3. 出，为下一个窗口做准备
            dx, dy = DIRS[s[left]]
            x -= dx
            y -= dy

        return len(st)

