S = input()

for i in range(97, 123):
    if chr(i) not in S:
        print(-1, end=" ")
        continue
    for j in range(len(S)):
        if chr(i) == S[j]:
            print(j, end=" ")
            break