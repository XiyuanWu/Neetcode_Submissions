import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        # Add original index to each task:
        # [enqueueTime, processingTime, index]
        tasks = [
            [enqueue, process, i]
            for i, (enqueue, process) in enumerate(tasks)
        ]

        # Sort by arrival/enqueue time
        tasks.sort()

        heap = []       # (processingTime, index)
        res = []

        time = 0
        i = 0
        n = len(tasks)

        while i < n or heap:

            # If CPU has nothing available,
            # jump time directly to the next task's arrival time
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # Add ALL tasks that have already arrived
            while i < n and tasks[i][0] <= time:
                enqueue, process, index = tasks[i]

                # Heap chooses:
                # 1. smallest processing time
                # 2. smaller index if tied
                heapq.heappush(heap, (process, index))

                i += 1

            # Choose shortest available task
            process, index = heapq.heappop(heap)

            # Record which task CPU processed
            res.append(index)

            # CPU is busy for 'process' amount of time
            time += process

        return res