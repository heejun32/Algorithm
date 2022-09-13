import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(a):
            if a in traced:
                return False
            if a in visited:
                return True
            
            traced.add(a)

            for b in graph[a]:
                if not dfs(b):
                    return False
            traced.remove(a)
            visited.add(a)
            
            return True
        
        graph = collections.defaultdict(list)
        for a, b in prerequisites:
            graph[a].append(b)
        
        traced = set()
        visited = set()
        
        # chek the cyclic
        for a in list(graph):
            if not dfs(a):
                return False
            
        return True
        