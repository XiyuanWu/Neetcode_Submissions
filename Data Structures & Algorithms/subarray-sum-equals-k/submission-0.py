class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1

        total = 0
        result = 0

        for num in nums:
            total += num

            need = total - k
            result += count[need]

            count[total] += 1

        return result