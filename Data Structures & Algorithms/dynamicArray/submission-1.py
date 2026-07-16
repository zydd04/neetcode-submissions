class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = []*capacity
        self.size = 0
    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if not self.array[i]:
            self.size += 1
        self.array[i] = n

    def pushback(self, n: int) -> None:
        self.size += 1
        if self.size > self.capacity:
            self.resize()
            self.array.append(n)
        else:
            self.array.append(n)

    def popback(self) -> int:
        self.size -= 1
        return self.array.pop()
    def resize(self) -> None:
        self.array = self.array + []*self.capacity
        self.capacity = self.capacity*2
    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
