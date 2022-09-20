import collections


class Solution:
    '''
    Time Complexity is O(ElogE) beacause of sorted(E)
    Space Complexity is O(E)

    '''
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop())
            routes.append(a)
        
        # make a graph
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
 
        routes = []
        dfs("JFK")
        
        return routes[::-1]