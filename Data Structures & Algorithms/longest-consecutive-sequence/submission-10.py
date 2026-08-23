class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        seen = set(nums)
        result = 0

        for i in nums:
            if i-1 not in seen:
                curr = 1

                while i + curr in seen:
                    curr += 1

                result = max(result, curr)

        return result