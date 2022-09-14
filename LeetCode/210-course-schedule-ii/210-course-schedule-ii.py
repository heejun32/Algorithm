import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        indegree = [0] * numCourses
        answer = []
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        def dfs(course):
            answer.append(course)
            indegree[course] -= 1
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    dfs(next_course)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        
        return answer if len(answer) == numCourses else []