class RideSharingSystem:
    def __init__(self):
        self.riders = deque()
        self.drivers = deque()
        self.waiting_riders = set()

    def addRider(self, riderId: int) -> None:
        self.riders.append(riderId)
        self.waiting_riders.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.drivers.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        # 弹出队列中的已取消乘客
        while self.riders and self.riders[0] not in self.waiting_riders:
            self.riders.popleft()
        # 没有乘客或者司机
        if not self.riders or not self.drivers:
            return [-1, -1]
        # 配对（这里没有删除 waiting_riders 中的乘客编号，面试的话建议写上删除的逻辑）
        return [self.drivers.popleft(), self.riders.popleft()]

    def cancelRider(self, riderId: int) -> None:
        self.waiting_riders.discard(riderId)

