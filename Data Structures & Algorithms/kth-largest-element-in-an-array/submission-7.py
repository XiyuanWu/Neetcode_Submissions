class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        result = []
        for i in range(len(nums)):
            result.append(heapq.heappop(nums))
        return result[-k]