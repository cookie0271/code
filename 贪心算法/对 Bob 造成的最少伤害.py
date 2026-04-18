class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        a = [((h - 1) // power + 1, d) for h, d in zip(health, damage)]
        a.sort(key=lambda p: p[0] / p[1])

        ans = s = 0
        for k, d in a:
            s += k
            ans += s * d
        return ans
