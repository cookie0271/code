class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if len(token) > 1 or token[0].isdigit():  # token 是数字
                st.append(int(token))
                continue

            x = st.pop()
            if token == '+':
                st[-1] += x
            elif token == '-':
                st[-1] -= x
            elif token == '*':
                st[-1] *= x
            else:
                # 题目要求除法向零取整，但 // 是向下取整
                st[-1] = trunc(st[-1] / x)  # 不用浮点数的写法见【Python3 写法二】
        return st[0]

