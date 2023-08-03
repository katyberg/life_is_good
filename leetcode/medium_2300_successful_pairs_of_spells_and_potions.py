class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Intuition:
        # Brute force: O(M*N)
        # Binary search: O(MlogM)+O(NlogM) = O((M+N)logM)
        # Still big difference:
        # Imagine both M and N are 1M -> O(M*N)=>10^12 (1T), but 2M*log(1M)=>12M!!!!
        # We BS to find the "insertion point" which gives us number of elements after

        # spells = [5,1,3], potions = [1,2,3,4,5], success = 7
        # 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
        # This function will return 1.
        # (7/5 = 1.4 which is less than item at index 1 so insertion point has index 1)
        # 0 <= return value <= m
        # also assuming potions is sorted
        # insertion point means the index at the insertion point is the next bigger value

        # IMPORTNAT!!!! BELOW FUNCTION IS WRONG!!!! THERE ARE DUPLICATES!!!!
        # def bs_insertion_index(potions: List[int], target: float):
        #     m = len(potions)
        #     left = 0
        #     right = m - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if potions[mid] == target:
        #             return mid
        #         elif potions[mid] > target:  # go left
        #             right = mid - 1
        #         else:  # go right
        #             left = mid + 1
        #     # if we drop out here, left > right, left is the insertion point!!!!
        #     # remember the contract for the function is to return m if exceeding m.
        #     # in the case where all items are greater than target, this funciton will return 0.
        #     # if left >= m:
        #     #     return m
        #     return left

        # THIS WORKS TOO.... WEIRD????
        # def bs_insertion_index(arr, target):
        #     left = 0
        #     right = len(arr) - 1
        #     while left <= right:
        #         mid = (left + right) // 2
        #         if arr[mid] < target:
        #             left = mid + 1
        #         else:  # >=
        #             right = mid - 1
        #     return left

        # FIND LEFT-MOST INSERTION POINT
        def bs_insertion_index(arr, target):
            left = 0
            right = len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left
        
        # # FIND RIGHT-MOST INSERTION POINT <= THIS DOES NOT WORK BECAUSE WE WANT LEFT-MOST!!!!
        # def bs_insertion_index(arr, target):
        #     left = 0
        #     right = len(arr)
        #     while left < right:
        #         mid = (left + right) // 2
        #         if arr[mid] > target:
        #             right = mid
        #         else:
        #             left = mid + 1
        #     return left
        
        n = len(spells)
        m = len(potions)
        result = []
        potions.sort()  # O(MlogM)
        for spell in spells:
            target = success / spell
            insertion_index = bs_insertion_index(potions, target)
            num_successful_potions = m - insertion_index  # 0 <= return value <= m
            result.append(num_successful_potions)
        return result

