class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in invocations:
            g[x].append(y)

        # 收集所有可疑方法
        suspicious = set()
        def dfs(x: int) -> None:
            suspicious.add(x)
            for y in g[x]:
                if y not in suspicious:  # 避免无限递归
                    dfs(y)
        dfs(k)

        # 检查是否有【非可疑方法】->【可疑方法】的边
        for x, y in invocations:
            if x not in suspicious and y in suspicious:
                # 无法移除可疑方法
                return list(range(n))

        # 移除所有可疑方法
        return list(set(range(n)) - suspicious)

