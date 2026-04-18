class Solution:
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0:
            return -1
        ans = 0
        hp = 1
        h = []
        for x in nums:
            if x < 0:
                heappush(h, x)
            hp += x
            if hp < 1:
                # 这意味着 x < 0，所以前面必然会把 x 入堆
                # 所以堆必然不是空的，并且堆顶 <= x
                hp -= heappop(h)  # 反悔
                ans += 1
        return ans
