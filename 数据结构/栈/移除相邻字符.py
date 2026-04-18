# 更快的写法见【Python3 写法二】
def is_consecutive(x: str, y: str) -> bool:
    d = abs(ord(x) - ord(y))
    return d == 1 or d == 25

class Solution:
    def resultingString(self, s: str) -> str:
        st = []
        for b in s:
            if st and is_consecutive(b, st[-1]):
                st.pop()
            else:
                st.append(b)
        return ''.join(st)

