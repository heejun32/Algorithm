import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            answer.append(a)
        
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
                    
        answer = []
        dfs("JFK")
        
        return answer[::-1]