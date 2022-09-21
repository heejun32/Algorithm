from typing import List


def solution(arr1: List[List[int]], arr2: List[List[int]]) -> List[List[int]]:
    '''
    Time Complexity is O(L * N * M)
    Space Complxity is O(L * N)
    ''' 
    l, n, m = len(arr1), len(arr2[0]), len(arr2)
    answer = [[0] * n for _ in range(l)]
    
    for i in range(l):
        for j in range(n):
            for k in range(m):
                answer[i][j] += arr1[i][k] * arr2[k][j] 
    
    return answer