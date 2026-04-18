class Router:
    def __init__(self, memoryLimit: int):
        self.memory_limit = memoryLimit
        self.packet_q = deque()  # packet 队列
        self.packet_set = set()  # packet 集合
        self.dest_to_timestamps = defaultdict(deque)  # destination -> [timestamp]

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        self.packet_set.add(packet)
        if len(self.packet_q) == self.memory_limit:  # 太多了
            self.forwardPacket()
        self.packet_q.append(packet)  # 入队
        self.dest_to_timestamps[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.packet_q:
            return []
        packet = self.packet_q.popleft()  # 出队
        self.packet_set.remove(packet)
        self.dest_to_timestamps[packet[1]].popleft()
        return packet  # list(packet)

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.dest_to_timestamps[destination]
        left = bisect_left(timestamps, startTime)  # deque 访问不是 O(1) 的，可以看另一份代码【Python3 list】
        right = bisect_right(timestamps, endTime)
        return right - left

