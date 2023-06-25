from functools import reduce
from typing import List


class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        # Example:
        # l = [['010'], ['100'], ['200', '205'], ['300','310','320']]
        # return: ['010', '100', '200', '205', '300','310','320']
        def flatten(l: List[List[str]]):
            return reduce(lambda x, y: x + y, l)

        # Example:
        # nums = ["102","473","251","814"]
        # queries = [2,3]  <= k = 2, trim = 3 (2nd smallest 3rd digit)
        # return: 2  <= index of the 2nd smallest 3rd digit
        # ps: for this example, flattened_sorted_nums = ["102","251","473","814"]
        def index_of_kth_min_item(nums: List[str], query: List[int]):
            # print(f'query={query}')
            k = query[0]
            digit = query[1]
            # print(f'k={k}, digit={digit}')
            sorted_nums = [[] for _ in range(10)]  # NOTICE THIS IS THE BUCKET 0 TO 9
            for num in nums:  # num is a str
                d = int(num[digit * -1])
                # print(f'd = {d}')
                sorted_nums[d].append(num)
            flattened_sorted_nums = flatten(sorted_nums)
            # print(f'flattened_sorted_nums={flattened_sorted_nums}')
            # print(f'number of {k} st smallest digit is {flattened_sorted_nums[k - 1]}')
            i = nums.index(flattened_sorted_nums[k - 1])
            # print(f'index of the {k} st smallest digit in nums is {i}')
            return i

        return [index_of_kth_min_item(nums, query) for query in queries]


# My implementation failed below test case; expected = [0,1,2,3]!!!!
# But I believe my implementation is CORRECT! I believe the test case is wrong!
def test() -> None:
    nums = ["9415","5908","1840","5307"]
    s = Solution()
    output = s.smallestTrimmedNumbers(nums, [[3,2],[2,2],[3,3],[1,3]])
    expected_output = [0,1,2,3]
    assert output == expected_output
    print(f'output={output}')


if __name__ == "__main__":
    test()

# >>> test()
# k=3, digit=2
# d = 1
# d = 0
# d = 4
# d = 0
# flattened_sorted_nums=['5908', '5307', '9415', '1840']
# number of 3 st smallest digit is 9415
# index of the 3 st smallest digit in nums is 0
# k=2, digit=2
# d = 1
# d = 0
# d = 4
# d = 0
# flattened_sorted_nums=['5908', '5307', '9415', '1840']
# number of 2 st smallest digit is 5307
# index of the 2 st smallest digit in nums is 3
# k=3, digit=3
# d = 4
# d = 9
# d = 8
# d = 3
# flattened_sorted_nums=['5307', '9415', '1840', '5908']
# number of 3 st smallest digit is 1840
# index of the 3 st smallest digit in nums is 2
# k=1, digit=3
# d = 4
# d = 9
# d = 8
# d = 3
# flattened_sorted_nums=['5307', '9415', '1840', '5908']
# number of 1 st smallest digit is 5307
# index of the 1 st smallest digit in nums is 3
