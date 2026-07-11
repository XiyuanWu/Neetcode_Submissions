class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window = []
        length = float("inf")

        l = 0
        for r in range(len(nums)):
            window.append(nums[r])

            while sum(window) >= target:
                length = min(length, len(window))
                window.pop(0)
                l += 1

        if length == float("inf"):
            return 0

        return length