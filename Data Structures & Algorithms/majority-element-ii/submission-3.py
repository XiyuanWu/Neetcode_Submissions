class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)
        result = []

        for i in nums:
            count[i] += 1

        for i in count:
            if count[i] > len(nums) // 3:
                result.append(i)

        return result