class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # index_dict = {}
        # for i in range(len(nums)):
        #     index_dict[nums[i]] = i
        # for i, num in enumerate(nums):
        #     counter_num = target - num
        #     if counter_num in index_dict and index_dict[counter_num] != i:
        #         return [i, index_dict[counter_num]]  # guarentee to have exactly one solution

        # IMPORTANT! WE CAN ACTUALLY DO IT IN ONE PASS!!!!
        # BECAUSE IF THERE ARE TWO NUMBERS THAT COMPLEMENT EACH OTHER, IF I AM AT 2 AND LOOKING BACK
        # I DO NOT FIND THE MATCH, I WILL FIND IT WHEN I LOOK BACK AT 8!!!!
        # ....2....8.... <= TARGET=10
        index_dict = {}
        for i in range(len(nums)):
            counter_num = target - nums[i]
            if counter_num in index_dict:
                return [i, index_dict[counter_num]]  # guarentee to have exactly one solution
            index_dict[nums[i]] = i

