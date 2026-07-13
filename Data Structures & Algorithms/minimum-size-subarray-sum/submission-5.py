class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = []
        result = float("inf")

        l = 0
        for r in range(len(nums)):
            window.append(nums[r])

            while sum(window) >= target:
                result = min(result, len(window))
                window.pop(0)
                l += 1

        if result == float("inf"):
            return 0

        return result