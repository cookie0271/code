class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # 用于模拟计算机的递归
        res = ''
        k = 0
        for c in s:
            if c.isalpha():
                res += c
            elif c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                # 模拟递归
                # 在递归之前，把当前递归函数中的局部变量 res 和 k 保存到栈中
                stack.append((res, k))
                # 递归，初始化 res 和 k
                res = ''
                k = 0
            else:  # ']'
                # 递归结束，从栈中恢复递归之前保存的局部变量
                pre_res, pre_k = stack.pop()
                # 此时 res 是下层递归的返回值，将其重复 pre_k 次，拼接到递归前的 pre_res 之后
                res = pre_res + res * pre_k
        return res

