class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        """
        #选或不选
        path = []
        self.queue = []
        def dfs(i):
            if i ==len(characters):
                if len(path)==combinationLength:
                    self.queue.append(''.join(path))
                return 
            #要求有序必须先选
            path.append(characters[i])
            dfs(i+1)
            path.pop()
            #不选
            dfs(i+1)
        dfs(0)
        """
        """
        #枚举选那个
        path = []
        self.queue = []
        def dfs(i):
            if len(path) == combinationLength:
                self.queue.append(''.join(path))
                return 
            for j in range(i, len(characters)):
                path.append(characters[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        """
        #库函数
        self.queue = list(map(lambda x : ''.join(x), combinations(characters, combinationLength)))


    def next(self) -> str:
        return self.queue.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.queue)!=0
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
