N = int(input())
GRADES = list(map(int, input().split()))

def solution(N, GRADES):
    highest_grade = max(GRADES)

    for i in range(N):
        GRADES[i] = (GRADES[i] / highest_grade) * 100

    answer = sum(GRADES) / len(GRADES)
    return answer

print(solution(N, GRADES))