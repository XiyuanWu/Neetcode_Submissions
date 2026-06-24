class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        result = []

        for i in nums:
            count[i] += 1

        for num in count:
            if count[num] > len(nums) // 3:
                result.append(num)

        return result
