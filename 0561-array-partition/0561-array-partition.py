class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pointer = 0
        total = 0

        while pointer < len(nums):
            total += nums[pointer]
            pointer += 2
        return total