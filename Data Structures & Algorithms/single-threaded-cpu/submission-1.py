import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        tasks = [
            [enqueue, process, i]
            for i, (enqueue, process) in enumerate(tasks)
        ]

        tasks.sort()

        heap = []
        res = []

        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            while i < n and tasks[i][0] <= time:
                enqueue, process, index = tasks[i]
                heapq.heappush(heap, (process, index))
                i += 1

            process, index = heapq.heappop(heap)
            res.append(index)
            time += process

        return res