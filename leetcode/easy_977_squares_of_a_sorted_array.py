from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Use library (but defeat the purpose):
        return sorted(list(map(lambda x: x ** 2, nums)))

        # Brute force:
        # loop through array and square each item O(n),
        # then sort the result array O(N^2) for insertion, O(NlogN) for Heap, O(N) for bucket sort

        # Two-pointer approach: runtime O(N), space O(N)
        # Important: nums is sorted in non-decreasing order.
        # Test case: [-3, -2, -1, 4, 5, 6]
        # Test case: [-3]  # 1 <= nums.length <= 104

        n = len(nums)
        l = 0
        r = n - 1
        result = []
        i = n - 1  # index into result list
        while l <= r:
            abs_l_num = abs(nums[l])
            abs_r_num = abs(nums[r])

            if abs_l_num >= abs_r_num:
                result[i] = abs_l_num ** 2
                l += 1
            else:
                result[i] = abs_r_num ** 2
                r -= 1
            i -= 1
        return result


def test() -> None:
    nums = [-3, -2, -1, 4, 5, 6]
    s = Solution()
    output = s.sortedSquares(nums)
    expected_output = [1, 4, 9, 16, 25, 36]
    assert output == expected_output
    print(f'output={output}')

    nums_2 = [-3]
    output_2 = s.sortedSquares(nums_2)
    expected_output_2 = [9]
    assert output_2 == expected_output_2
    print(f'output_2={output_2}')


if __name__ == "__main__":
    test()
