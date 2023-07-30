import heapq
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # This is greedy, we can just sort or use heap
        
        asteroids.sort()
        for asteroid in asteroids:
            if asteroid <= mass:
                mass += asteroid
            else:
                return False
        return True

        # heapq.heapify(asteroids)
        # while len(asteroids):
        #     smallest = heapq.heappop(asteroids)
        #     if smallest <= mass:
        #         mass += smallest
        #     else:
        #         return False
        # return True

