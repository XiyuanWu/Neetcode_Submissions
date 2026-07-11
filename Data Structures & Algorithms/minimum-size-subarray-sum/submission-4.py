class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        length = float("inf")

        l = 0
        for r in range(len(nums)):
            sum += nums[r]

            while sum >= target:
                length = min(length, r - l + 1)
                sum -= nums[l]
                l += 1

        if length == float("inf"):
            return 0

        return length