class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for i in range(numCourses)]
        for course, preq in prerequisites:
            graph[course].append(preq)

        visited = set()
        completed = set()
        output = []

        def dfs(course):
            if course in visited: return False
            if course in completed: return True

            visited.add(course)

            for preq in graph[course]:
                if not dfs(preq):
                    return False

            visited.remove(course)
            completed.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return output