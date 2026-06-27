class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        nums.sort()
        result = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            remain = limit - nums[right]
            right -= 1
            result += 1

            if left <= right and remain >= nums[left]:
                left += 1

        return result