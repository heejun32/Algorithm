import sys
'''
Time Complexity is O(N^2)
Space Complexity is O(N^2)
'''
def solution() -> None:
    N, M = map(int, sys.stdin.readline().split())
    TABLE = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    # Table 누적합 계산 = dp
    for row in range(1, N + 1):
        for col in range(1, N + 1):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1] + TABLE[row - 1][col - 1]

    for _ in range(M):
        x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
        answer = dp[x2][y2] - dp[x2][y1 - 1] - dp[x1 - 1][y2] + dp[x1 - 1][y1 - 1]
        print(answer)

    return None


solution()
