class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0
        print(json.dumps(counts, indent=4))

        for num in nums:
            curr += num % 2
            ans += counts[curr - k]
            counts[curr] += 1
            print(f'num={num}, curr={curr}, ans={ans}')
            print(json.dumps(counts, indent=4))

        return ans

        # {
        #     "0": 1
        # }
        # num=2, curr=0, ans=0
        # {
        #     "0": 2,
        #     "-2": 0
        # }
        # num=2, curr=0, ans=0
        # {
        #     "0": 3,
        #     "-2": 0
        # }
        # num=2, curr=0, ans=0
        # {
        #     "0": 4,
        #     "-2": 0
        # }
        # num=1, curr=1, ans=0
        # {
        #     "0": 4,
        #     "-2": 0,
        #     "-1": 0,
        #     "1": 1
        # }
        # num=2, curr=1, ans=0
        # {
        #     "0": 4,
        #     "-2": 0,
        #     "-1": 0,
        #     "1": 2
        # }
        # num=2, curr=1, ans=0
        # {
        #     "0": 4,
        #     "-2": 0,
        #     "-1": 0,
        #     "1": 3
        # }
        # num=1, curr=2, ans=4
        # {
        #     "0": 4,
        #     "-2": 0,
        #     "-1": 0,
        #     "1": 3,
        #     "2": 1
        # }
        # num=2, curr=2, ans=8
        # {
        #     "0": 4,
        #     "-2": 0,
        #     "-1": 0,
        #     "1": 3,
        #     "2": 2
        # }
        # num=2, curr=2, ans=12
        # {
        #     "0": 4,
        #     "-2": 0,
        #     "-1": 0,
        #     "1": 3,
        #     "2": 3
        # }
        # num=2, curr=2, ans=16
        # {
        #     "0": 4,
        #     "-2": 0,
        #     "-1": 0,
        #     "1": 3,
        #     "2": 4
        # }

        # THE SLIDING WINDOW SOLUTION BELOW IS WRONG!!!!
        # THE REASON WE CANNOT USE SLIDING WINDOW FOR THIS PROBLEM IS BECAUSE
        # WE REALLY NEED TO CONSIDER THE ENTIRE ARRAY, ALL COMBINATIONS TO CHECK CONSTRAINT.
        # SLIDING WINDOW WILL KEEP MOVING ON, WHICH DOES NOT CONTAIN ALL COMBINATIONS.
        # SO WHAT DO WE THINK ABOUT? HASH TABLE!!!!
        # Example: nums=[2,2,2,1,2,2,1,2,2,2], k=2 => there are 16 combinations
        #        1,2,2,1
        #     2, 1,2,2,1
        #   2,2, 1,2,2,1
        # 2,2,2, 1,2,2,1
        #        1,2,2,1, 2
        #        1,2,2,1, 2,2
        #        1,2,2,1, 2,2,2
        #     2, 1,2,2,1, 2
        #     2, 1,2,2,1, 2,2
        #     2, 1,2,2,1, 2,2,2
        #   2,2, 1,2,2,1, 2
        #   2,2, 1,2,2,1, 2,2
        #   2,2, 1,2,2,1, 2,2,2
        # 2,2,2, 1,2,2,1, 2
        # 2,2,2, 1,2,2,1, 2,2
        # 2,2,2, 1,2,2,1, 2,2,2
        # # iterate through the array with two pointers
        # left = right = 0
        # num_of_odd = 0
        # ans = 0
        # # constraint is num_of_odd <= k
        # # increment the right pointer until constraint is broken, 
        # # at which point increment the left pointer.
        # # constraint is "number of odd number", odd number is (num % 2)
        # for right in range(len(nums)):
        #     num_of_odd += (nums[right] % 2)  # 0 if even, 1 if odd
        #     while num_of_odd > k:
        #         num_of_odd -= (nums[left] % 2)  # Don't forget this!
        #         left += 1
        #     if num_of_odd == k:
        #         ans += 1
        # return ans

