class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for i in nums:
            count[i] += 1

        return sorted(count, key=count.get, reverse=True)[:k]