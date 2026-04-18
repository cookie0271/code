func winnerOfGame(colors string) bool {
	cnt := [2]int{}
	for i, n := 0, len(colors); i < n; {
		i0 := i
		c := colors[i0]
		for i < n && colors[i] == c {
			i++ // 注意这里 i 就是外层循环的 i，所以复杂度是 O(n) 的
		}
		if l := i - i0; l > 2 {
			cnt[c-'A'] += l - 2
		}
	}
	return cnt[0] > cnt[1]
}
