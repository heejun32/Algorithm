import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Time Complexity is O(N + E)
        Space Complexity is O(N + E)
        
        '''
        graph = collections.defaultdict(list)
        queue = collections.deque()
        indegree = [0] * numCourses
        answer = []
        
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            answer.append(course)
            for next_course in graph[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        
        return answer if len(answer) == numCourses else []
        
            