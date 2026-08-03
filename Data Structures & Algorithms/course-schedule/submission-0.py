class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [ [] for i in range(numCourses)]

        for course, preq in prerequisites:
            graph[course].append(preq)

        visited = set()
        completed = set()

        def dfs(course):
            if course in visited: return False
            if course in completed: return True

            visited.add(course)

            for preq in graph[course]:
                if not dfs(preq):
                    return False

            visited.remove(course)
            completed.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True