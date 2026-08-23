class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(nums):
            if nums[r] > nums[l]:
                profit = nums[r] - nums[l]
                maxP = max(profit, maxP)
            else:
                l = r
            r += 1

        return maxP