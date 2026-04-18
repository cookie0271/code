class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def check(k: int) -> bool:
            # 贪心：用最强的 k 名工人，完成最简单的 k 个任务
            i, p = 0, pills
            valid_tasks = deque()
            for w in workers[-k:]:  # 枚举工人
                # 在吃药的情况下，把能完成的任务记录到 valid_tasks 中
                while i < k and tasks[i] <= w + strength:
                    valid_tasks.append(tasks[i])
                    i += 1
                # 即使吃药也无法完成任务
                if not valid_tasks:
                    return False
                # 无需吃药就能完成（最简单的）任务
                if w >= valid_tasks[0]:
                    valid_tasks.popleft()
                    continue
                # 必须吃药
                if p == 0:  # 没药了
                    return False
                p -= 1
                # 完成（能完成的）最难的任务
                valid_tasks.pop()
            return True

        left, right = 0, min(len(tasks), len(workers)) + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left

