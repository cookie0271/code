class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append((target, 0))
        ans = pre_position = 0
        cur_fuel = startFuel
        fuel_heap = []  # 下面把堆中元素取反，当作最大堆用
        for position, fuel in stations:
            cur_fuel -= position - pre_position  # 每行驶 1 英里用掉 1 升汽油
            while fuel_heap and cur_fuel < 0:  # 没油了
                cur_fuel -= heappop(fuel_heap)  # 选油量最多的油桶
                ans += 1
            if cur_fuel < 0:  # 无法到达
                return -1
            heappush(fuel_heap, -fuel)  # 留着后面加油
            pre_position = position
        return ans

