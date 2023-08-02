class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1  # don't need in this problem because 1 <= nums.length <= 104
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1  # not found if got here

