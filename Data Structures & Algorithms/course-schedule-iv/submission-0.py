class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for preq, course in prerequisites:
            graph[preq].append(course)

        def dfs(course, visited):
            for n in graph[course]:
                if n not in visited:
                    visited.add(n)
                    dfs(n, visited)

        reachable = {}

        for course in range(numCourses):
            visited = set()
            dfs(course, visited)
            reachable[course] = visited

        result = []
        for a, b in queries:
            result.append(b in reachable[a])

        return result