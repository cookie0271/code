class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heapify_max(gifts)  # 原地堆化
        while k and gifts[0] > 1:
            heapreplace_max(gifts, isqrt(gifts[0]))  # 直接修改堆顶
            k -= 1
        return sum(gifts)

