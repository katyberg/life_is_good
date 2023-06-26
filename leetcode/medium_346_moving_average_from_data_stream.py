from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.queue = deque()
        self.size = size
        self.running_sum = 0

    # Keeping a running sum, we beat ~54% of the people :-)
    def next(self, val: int) -> float:
        self.queue.append(val)
        self.running_sum += val
        while len(self.queue) > self.size:
            popped = self.queue.popleft()
            self.running_sum -= popped
        return self.running_sum / len(self.queue)  
    
    # # Without keep tracking of the sum, we beat ~66% of people :-)
    # def next(self, val: int) -> float:
    #     self.queue.append(val)
    #     while len(self.queue) > self.size:
    #         self.queue.popleft()
    #     return sum(self.queue) / len(self.queue)            


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
