class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        j, m = 0, len(trainers)
        for i, p in enumerate(players):
            while j < m and trainers[j] < p:
                j += 1
            if j == m:  # 无法找到匹配的训练师
                return i
            j += 1  # 匹配一位训练师
        return len(players)  # 所有运动员都有匹配的训练师

