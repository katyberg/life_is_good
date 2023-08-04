class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # This problem really needs a visual!
        # Example: [1,2,5,9] threshold=6
        # divisor => formula => sum
        #                           <-------- threshold > sum(nums), answer is 1
        #     1   => 1+2+5+9 => 17  <---- this is the max dsum
        #     2   => 1+1+3+5 => 10
        #     3   => 1+1+2+3 => 7
        #     4   => 1+1+2+3 => 7
        #     5   => 1+1+2+2 => 6  <-------- this is the threshold for this example
        #     6   => 1+1+1+2 => 5
        #     7   => 1+1+1+2 => 5
        #     8   => 1+1+1+2 => 5
        #     9   => 1+1+1+1 => 4  <---- this is the min dsum
        #  i > 9  => 1+1+1+1 => 4  <==== all divisors larger than max(nums) have dsum 4
        #                                ^ if threshold < len(nums) there is no answer

        # domain range is min and max of the array
        def calculate_division_sum(divisor):
            division_sum = 0
            for num in nums:
                division_sum += math.ceil(num / divisor)
            return division_sum

        # THINK ABOUT USE CASE [19] threshold=5
        # all divisor over max(nums) will give sum(nums)
        # in which case the min divisor is 1
        if threshold > sum(nums):
            return 1
        # IMPORTANT!!!! HAS TO START WITH 1 WHICH GIVES THE MAX SUM!
        # left = min(nums)  # WRONG!!!!
        left = 1
        right = max(nums)
        # while left < right:  # IMPORTANT!!!! HAVE TO HAVE <= HERE NOT <!!!!
        while left <= right:
            mid = (left + right) // 2
            if calculate_division_sum(mid) <= threshold:  # go left
                right = mid - 1
            else:  # go right
                left = mid + 1
        return left

