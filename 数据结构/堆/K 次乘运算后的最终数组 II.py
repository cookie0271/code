class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:  # 数组不变
            return nums

        MOD = 1_000_000_007
        n = len(nums)
        mx = max(nums)

        # 打表，计算出最小的 e 满足 multiplier^e >= 2^i
        e_pow_m = []
        pow_m = pow2 = 1
        e = 0
        while pow2 <= mx:
            if pow_m < pow2:  # 由于 multiplier >= 2，这里只需写 if 而不是 while
                pow_m *= multiplier
                e += 1
            e_pow_m.append((e, pow_m))
            pow2 <<= 1

        # 把每个数都操作到 >= mx
        left = k
        clone = nums.copy()
        mx_len = mx.bit_length()
        for i, x in enumerate(nums):
            e, pow_m = e_pow_m[mx_len - x.bit_length()]
            if pow_m // multiplier * x >= mx:  # 多操作了一次
                pow_m //= multiplier
                e -= 1
            elif x * pow_m < mx:  # 少操作了一次
                pow_m *= multiplier
                e += 1
            left -= e
            if left < 0:
                break
            nums[i] *= pow_m

        if left < 0:
            # 暴力模拟
            h = [(x, i) for i, x in enumerate(clone)]
            heapify(h)
            for _ in range(k):
                x, i = h[0]
                heapreplace(h, (x * multiplier, i))
            for x, j in h:
                clone[j] = x % MOD
            return clone

        # 剩余的操作可以直接用公式计算
        k = left
        pow1 = pow(multiplier, k // n, MOD)
        pow2 = pow1 * multiplier % MOD
        for i, (x, j) in enumerate(sorted((x, i) for i, x in enumerate(nums))):
            nums[j] = x * (pow2 if i < k % n else pow1) % MOD
        return nums

