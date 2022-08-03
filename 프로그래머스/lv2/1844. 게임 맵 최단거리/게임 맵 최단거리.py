from collections import deque

def bfs(maps, x, y):
    n, m = len(maps), len(maps[0])
    queue = deque()
    queue.append([x, y])
    
    # bfs 탐색
    while queue:
        x, y = queue.popleft()
        # 동서남북 이동
        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 이동할때마다 이동한 칸 증가 및 경로 추가
                maps[nx][ny] = maps[x][y] + 1
                queue.append([nx, ny])
                # 정답 확인
                if nx == n - 1 and ny == m - 1:
                    return maps[nx][ny]
    return - 1
    

def solution(maps):
    answer = bfs(maps, 0, 0)
    return answer