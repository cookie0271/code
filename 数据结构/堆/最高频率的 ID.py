class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        cnt = defaultdict(int)
        h = []
        ans = []
        for x, f in zip(nums, freq):
            cnt[x] += f
            heappush_max(h, (cnt[x], x))
            while h[0][0] != cnt[h[0][1]]:  # 堆顶保存的数据已经发生变化
                heappop_max(h)  # 删除
            ans.append(h[0][0])
        return ans

