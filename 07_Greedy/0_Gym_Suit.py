def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n+1):
        if i not in lost: #안 잃어버린 학생
            answer += 1
        else:
            if i in reserve: #잃어버렸지만 여분도 있는 학생
                answer += 1
                reserve.remove(i)
                lost.remove(i)

    for i in lost: #잃어버리고 여분도 없어서 빌려야 하는 학생
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)

        elif i+1 in reserve:
            answer +=1
            reserve.remove(i+1)

    return answer

# 내 코드 - 반성할 점: 문제에 대한 해결을 어떻게 할 수 있을지 효율적인 생각을 해보자
def solution(n, lost, reserve):
    answer = 0
    n_list = [1] * n

    for r in reserve:
        n_list[r - 1] = 2

    for l in lost:
        n_list[l - 1] -= 1

    for i in range(0, len(n_list) - 1):
        if i == 0:
            if n_list[i] == 0:
                if n_list[i + 1] >= 2:
                    n_list[i] += 1
                    n_list[i + 1] -= 1

        elif n_list[i] == 0:
            if n_list[i - 1] >= 2:
                n_list[i] += 1
                n_list[i - 1] -= 1

            elif n_list[i + 1] >= 2:
                n_list[i] += 1
                n_list[i + 1] -= 1

        else:
            continue

    for i in n_list:
        if i >= 1:
            answer += 1

    return answer