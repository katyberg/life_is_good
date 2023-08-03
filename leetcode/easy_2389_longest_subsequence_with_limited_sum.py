class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # Ituition:
        # 1. sort nums, create prefix sum
        # 2. find right most insert of target
        # Ex: [4, 5, 2, 1] -> [1, 2, 4, 5] => [1, 3, 7, 12]
        #     queries = [3, 10, 21]
        #     answer  = [2, 3, 4]
        nums.sort()
        n = len(nums)
        prefix_sum = [nums[0]]  # 1 <= n <= 1000
        for i in range(1, n):
            prefix_sum.append(nums[i] + prefix_sum[-1])
        
        # IMPORTANT!!!! THIS FUNCTION COMES OUT OF THE BOX FOR PYTHON!!!!
        # IT IS bisect.bisect_right(prefix_sum, query)!!!!
        def binary_search_rightmost_insert_index(arr, target: int):
            l = 0
            r = n
            while l < r:
                m = (l + r) // 2
                if arr[m] == target:
                    return m + 1
                elif arr[m] > target:
                    r = m
                else:
                    l = m + 1
            return l
        
        result = []
        for query in queries:
            result.append(binary_search_rightmost_insert_index(prefix_sum, query))
            # Note we can just use bisect.bisect_right!
            # result.append(bisect.bisect_right(prefix_sum, query))
        return result

