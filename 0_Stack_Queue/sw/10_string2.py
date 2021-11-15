TEST_CASE = int(input())

for test in range(1, TEST_CASE + 1):
    N, M = map(int, input().strip().split())
    result = []

    # 배열 입력 받기
    arr = []
    for i in range(N):
        arr.append(input())

    # 가로 검색
    for r in range(N):
        for c in range(N - M + 1):
            if arr[r][c : c + M] == arr[r][c : c + M][::-1]:
                result.append(arr[r][c : c + M])

    # 세로 검색
    for r in range(N - M + 1):
        for c in range(N):
            c_lst = ""  # 열 단어 확인
            for i in range(M):
                c_lst = c_lst + arr[r+i][c]
            if c_lst == c_lst[::-1]:
                result.append(c_lst)

    print(f"#{test} {result[0]}")
# 굳이 join 함수 쓸 필요 없이 string 슬라이싱을 이용해 풀 수 있음