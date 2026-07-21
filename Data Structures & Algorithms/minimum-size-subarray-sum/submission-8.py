class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        total = 0
        result = float("inf")

        l = 0
        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                result = min(result, r - l + 1)
                total -= nums[l]
                l += 1

        if result == float("inf"):
            return 0

        return result
        