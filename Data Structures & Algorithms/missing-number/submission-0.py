class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = set(nums)
        missing = 0

        for i in seen:
            if missing in seen:
                missing += 1

        return missing