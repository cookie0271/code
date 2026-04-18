class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_idx = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_idx[email].append(i)

        def dfs(i: int) -> None:
            vis[i] = True
            for email in accounts[i][1:]:  # 遍历 i 的所有邮箱地址
                if email in email_set:
                    continue
                email_set.add(email)
                for j in email_to_idx[email]:  # 遍历所有包含该邮箱地址的账户下标 j
                    if not vis[j]:  # j 没有访问过
                        dfs(j)

        ans = []
        vis = [False] * len(accounts)
        for i, b in enumerate(vis):
            if not b:  # i 没有访问过
                email_set = set()  # 用于收集 DFS 中访问到的邮箱地址
                dfs(i)
                ans.append([accounts[i][0]] + sorted(email_set))
        return ans

