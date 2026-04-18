class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []
        path = [0] * 4  # path[i] 表示第 i 段（i 从 0 开始）的结束位置 + 1（右开区间，方便切片）

        # 分割 s[i] 到 s[n-1]，现在在第 j 段（j 从 0 开始），数值为 ip_val
        def dfs(i: int, j: int, ip_val: int) -> None:
            if i == n:  # s 分割完毕
                if j == 4:  # 必须有 4 段
                    a, b, c, _ = path
                    ans.append(f"{s[:a]}.{s[a:b]}.{s[b:c]}.{s[c:]}")
                return

            if j == 4:  # j=4 的时候必须分割完毕，不能有剩余字符
                return

            # 手动把字符串转成整数，这样字符串转整数是严格 O(1) 的
            ip_val = ip_val * 10 + int(s[i])
            if ip_val > 255:  # 不合法
                return

            # 不分割，不以 s[i] 为这一段的结尾
            if ip_val > 0:  # 无前导零
                dfs(i + 1, j, ip_val)

            # 分割，以 s[i] 为这一段的结尾
            path[j] = i + 1  # 记录这一段的结束位置 + 1
            dfs(i + 1, j + 1, 0)

        dfs(0, 0, 0)
        return ans

