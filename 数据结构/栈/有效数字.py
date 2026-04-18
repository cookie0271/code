class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)

        # 正负号
        i = 0
        if s[i] in "+-":
            i += 1

        # 指数符号之前，至多一个小数点，其余必须全是数字
        has_dot = has_digit = False
        while i < n and s[i] not in "eE":
            if s[i] == '.':
                if has_dot:  # 不能有两个小数点
                    return False
                has_dot = True
            elif '0' <= s[i] <= '9':
                has_digit = True
            else:
                return False
            i += 1

        # 必须有数字
        if not has_digit:
            return False

        # 指数符号之后，必须是整数
        if i < n and s[i] in "eE":
            i += 1

            # 正负号
            if i < n and s[i] in "+-":
                i += 1

            # 必须有数字
            if i == n:
                return False

            # 剩下的必须全是数字
            while i < n and '0' <= s[i] <= '9':
                i += 1

        # 如果 i < n 说明有非法字符，不是有效数字
        return i == n

