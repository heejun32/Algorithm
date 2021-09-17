test_cases = int(input())

for test_case in range(test_cases):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = list()
    for i in range(N - M + 1):
        ans.append(sum(arr[i: i + M]))

    print("#{} {}".format(test_case + 1, max(ans) - min(ans)))
