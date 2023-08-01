class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Test cases:
        # 1 <= people.length <= 5 * 104
        # 1 <= people[i] <= limit <= 3 * 104
        # people = [1], limit = 3
        # people = [3], limit = 3
        # people = [1,2], limit = 2
        # people = [1,2], limit = 3
        # people = [3,2,2,1], limit = 3

        people.sort()
        i, j = 0, len(people) - 1  # 1 <= people.length <= 5 * 104
        num_boat = 0
        while i < j:
            if people[i] + people[j] > limit:
                num_boat += 1  # put heaviest person on a boat by him/herself
                j -= 1
            else:  # <= limit
                num_boat += 1  # put them both in the same boat
                i += 1
                j -= 1
        if i == j:
            num_boat += 1  # last one person takes a single boat
        return num_boat

        # # This is more concise
        # while i <= j:
        #     ans += 1
        #     if people[i] + people[j] <= limit:
        #         i += 1
        #     j -= 1
        # return ans

