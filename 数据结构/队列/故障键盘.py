class Solution:
    def finalString(self, s: str) -> str:
        q = deque()
        tail = True
        for c in s:
            if c == 'i':
                tail = not tail  # 修改添加方向
            elif tail:  # 加尾部
                q.append(c)
            else:  # 加头部
                q.appendleft(c)
        return ''.join(q if tail else reversed(q))

