import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())
            rount.append(start)
                
        
        # {출발지: [도착지1, 도착지2, ...]} 저장
        graph = collections.defaultdict(list)
        for depart, arrive in sorted(tickets, reverse=True):
            graph[depart].append(arrive)
 
        rount = []
        dfs('JFK')
        return rount[::-1]
        