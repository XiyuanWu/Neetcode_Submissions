class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]
            first = account[1]

            for email in account[1:]:
                graph[first].add(email)
                graph[email].add(first)
                email_to_name[email] = name

        visited = set()
        result = []

        def dfs(email, group):
            if email in visited: return

            visited.add(email)
            group.append(email)

            for nei in graph[email]:
                dfs(nei, group)


        for email in graph:
            if email not in visited:
                group = []
                dfs(email, group)
                result.append([email_to_name[email]] + sorted(group))

        return result