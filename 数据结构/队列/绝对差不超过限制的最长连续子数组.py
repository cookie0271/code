class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque()
        max_q = deque()
        ans = left = 0

        for i, x in enumerate(nums):
            # 1. 右边入
            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(i)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(i)

            # 2. 左边出
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                left += 1
                if min_q[0] < left:  # 队首不在窗口中
                    min_q.popleft()
                if max_q[0] < left:  # 队首不在窗口中
                    max_q.popleft()

            # 3. 更新答案
            ans = max(ans, i - left + 1)

        return ans

