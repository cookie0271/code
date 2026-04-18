class Solution:
    # 计算这一组的得分（配对个数），以及剩余元素个数
    def calc(self, cnt: Dict[str, int]) -> Tuple[int, int]:
        sum_cnt = sum(cnt.values())
        max_cnt = max(cnt.values(), default=0)
        pairs = min(sum_cnt // 2, sum_cnt - max_cnt)
        return pairs, sum_cnt - pairs * 2

    def score(self, cards: List[str], x: str) -> int:
        cnt = Counter(cards)
        cnt_xx = cnt.pop(x + x, 0)
        cnt1 = {b: c for (a, b), c in cnt.items() if a == x}  # 统计 "x?" 中的 ? 的出现次数
        cnt2 = {a: c for (a, b), c in cnt.items() if b == x}  # 统计 "?x" 中的 ? 的出现次数

        pairs1, left1 = self.calc(cnt1)
        pairs2, left2 = self.calc(cnt2)
        ans = pairs1 + pairs2  # 不考虑 xx 时的得分

        # 把 xx 和剩下的 x? 和 ?x 配对
        # 每有 1 个 xx，得分就能增加一，但这不能超过剩下的 x? 和 ?x 的个数 left1+left2
        if cnt_xx > 0:
            mn = min(cnt_xx, left1 + left2)
            ans += mn
            cnt_xx -= mn

        # 如果还有 xx，就撤销之前的配对，比如 (ax,bx) 改成 (ax,xx) 和 (bx,xx)
        # 每有 2 个 xx，得分就能增加一，但这不能超过之前的配对个数 pairs1+pairs2
        # 由于这种方案平均每个 xx 只能增加 0.5 分，不如上面的，所以先考虑把 xx 和剩下的 x? 和 ?x 配对，再考虑撤销之前的配对
        if cnt_xx > 0:
            ans += min(cnt_xx // 2, pairs1 + pairs2)

        return ans

