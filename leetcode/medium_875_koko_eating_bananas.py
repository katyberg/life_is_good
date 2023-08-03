class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Intuition:
        # Domain space is 1 to max(piles) because Koko can eat at maximum the whole single pile
        # For each entry in domain space, we want to find the min successful entry
        # Successful means to be able to eat len(piles) bananas within h hours
        # Algo - binary search within domain space, each entry calculate whether or not successful
        
        # return True if koko can eat all bananas within h hours with the speed provided
        def successful(speed: int):
            total_hour = 0
            for pile in piles:
                total_hour += math.ceil(pile / speed)
            return total_hour <= h
        
        # DUH! I DO NOT NEED THIS DOMAIN SPACE AT ALL!!!!
        # THE INDEX ITSELF IS SUFFICIENT BECAUSE THE DOMAIN SPACE ITSELF IS 0 - N....
        # domain_space = [i for i in range(1, max(piles) + 1)]
        # # now binary search to find the min successful speed (bananas per hour)
        # left = 0
        # right = len(domain_space)
        # while left < right:
        #     mid = (left + right) // 2
        #     if successful(domain_space[mid]):  # go left
        #         right = mid
        #     else:
        #         left = mid + 1
        # return domain_space[left]

        left = 1  # 0 is invalid
        right = max(piles)
        while left < right:
            mid = (left + right) // 2
            if successful(mid):  # go left
                right = mid
            else:
                left = mid + 1
        return left

