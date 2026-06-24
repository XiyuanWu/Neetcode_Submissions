class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        missing = 1

        for i in nums:
            if i == missing:
                missing += 1

        return missing