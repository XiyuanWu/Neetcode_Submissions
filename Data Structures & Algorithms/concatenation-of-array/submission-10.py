class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []

        for i in nums:
            result.append(i)

        for j in nums:
            result.append(j)

        return result
