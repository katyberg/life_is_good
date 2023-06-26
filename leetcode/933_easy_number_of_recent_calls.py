from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()
    
    def ping(self, t: int) -> int:
        # self.queue.append(t)  # move to after removal
        # REMOVE ITEMS THAT ARE OUTSIDE OF t-3000 RANGE!!!!
        # BUT USE A WHILE LOOP!!!! CANN0T MUTATE THE STRING DURING ITERATION!!!!!!!!!!!!!!!!
        # for item in self.queue:
        while self.queue and self.queue[0] < t - 3000:
                self.queue.popleft()
        # maybe it is better to add this after the removal (probably does not matter though)
        self.queue.append(t)
        # What is left at this point is between t-3000 and t
        return len(self.queue)

    # # NOTE THAT WE CANNOT MUTATE THE LIST DURING ITERATION!!!!!!!!
    # # RuntimeError: deque mutated during iteration
    # #     for item in self.queue:
    # # Line 12 in ping (Solution.py)
    # #     result = obj.ping(
    # # Line 35 in __helper_select_method__ (Solution.py)
    # #     ret.append(__DriverSolution__().__helper_select_method__(method, params[index], obj))
    # # Line 73 in _driver (Solution.py)
    # #     _driver()
    # # Line 82 in <module> (Solution.py)
    # def ping(self, t: int) -> int:
    #     self.queue.append(t)
    #     # print(f'self.queue={self.queue}')
    #     result = []
    #     for item in self.queue:
    #         # REMOVE ITEMS THAT ARE OUTSIDE OF t-3000 RANGE!!!!
    #         if item < t - 3000:
    #             self.queue.popleft()
    #         # elif: item <= t and item >= t - 3000:
    #         else:  # since we keep removing item < t - 3000, all items left are >= t - 3000
    #             result.append(t)
    #     return len(result)






# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
