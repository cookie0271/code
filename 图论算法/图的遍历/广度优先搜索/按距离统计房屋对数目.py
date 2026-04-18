class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        if x > y:
            x, y = y, x

        diff = [0] * (n + 1)

        def add(l: int, r: int, v: int) -> None:
            if l > r: return
            diff[l] += v
            diff[r + 1] -= v

        def update(i: int, x: int, y: int) -> None:
            add(y - i, n - i, -1)  # 撤销 [y,n]
            dec = y - x - 1  # 缩短的距离
            add(y - i - dec, n - i - dec, 1)

            j = (x + y + 1) // 2 + 1
            add(j - i, y - 1 - i, -1)  # 撤销 [j, y-1]
            add(x - i + 2, x - i + y - j + 1, 1)

        def update2(i: int, x: int, y: int) -> None:
            add(y - i, n - i, -1)  # 撤销 [y,n]
            dec = (y - i) - (i - x + 1)  # 缩短的距离
            add(y - i - dec, n - i - dec, 1)

            j = i + (y - x + 1) // 2 + 1
            add(j - i, y - 1 - i, -1)  # 撤销 [j, y-1]
            add(i - x + 2, i - x + y - j + 1, 1)

        for i in range(1, n + 1):
            add(1, i - 1, 1)
            add(1, n - i, 1)
            if x + 1 >= y:
                continue
            if i <= x:
                update(i, x, y)
            elif i >= y:
                update(n + 1 - i, n + 1 - y, n + 1 - x)
            elif i < (x + y) // 2:
                update2(i, x, y)
            elif i > (x + y + 1) // 2:
                update2(n + 1 - i, n + 1 - y, n + 1 - x)

        return list(accumulate(diff))[1:]

