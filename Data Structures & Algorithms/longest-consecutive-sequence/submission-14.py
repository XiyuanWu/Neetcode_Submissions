class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        map = set(nums)
        result = 0

        for i in map:
            if i - 1 not in map:
                curr = 1

                while i + curr in map:
                    curr += 1

                result = max(result, curr)

        return result