class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1

        nums.sort()

        for i in nums:
            if i == missing:
                missing += 1

        return missing