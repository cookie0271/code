# 计算 nums 的每个长为 k 的窗口的最大值
# 时间复杂度 O(n)，其中 n 是 nums 的长度
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    ans = [0] * (len(nums) - k + 1)  # 窗口个数
    q = deque()  # 双端队列

    for i, x in enumerate(nums):
        # 1. 右边入
        while q and nums[q[-1]] <= x:
            q.pop()  # 维护 q 的单调性
        q.append(i)  # 注意保存的是下标，这样下面可以判断队首是否离开窗口

        # 2. 左边出
        left = i - k + 1  # 窗口左端点
        if q[0] < left:  # 队首离开窗口
            q.popleft()

        # 3. 在窗口左端点处记录答案
        if left >= 0:
            # 由于队首到队尾单调递减，所以窗口最大值就在队首
            ans[left] = nums[q[0]]

    return ans

