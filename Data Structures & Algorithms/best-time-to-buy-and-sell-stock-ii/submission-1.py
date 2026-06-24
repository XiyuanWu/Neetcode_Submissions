class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        total = 0

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                total += nums[i] - nums[i-1]
        return total