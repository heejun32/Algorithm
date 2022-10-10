import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Exception
        if n == 1:
            return [0]
        
        # 양방향 그래프 구성
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # 첫 번째 리프 노드 추가
        leaves = []
        for a in range(n):
            if len(graph[a]) == 1:
                leaves.append(a)
                
        # root 노트만 남을 때까지 반복 제거
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
            
        return leaves