class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        boat = 0

        while l <= r:
            remain = limit - nums[r]

            if nums[l] <= remain:
                l += 1

            boat += 1
            r -= 1

        return boat