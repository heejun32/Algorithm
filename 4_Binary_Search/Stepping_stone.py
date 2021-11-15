def solution(distance, rocks, n):
    rocks.sort()
    answer  = 0
    left    = 1
    right   = distance

    while (left <= right):
        del_rock = 0
        pre_rock = 0
        mid      = (left + right) // 2

        for rock in rocks:
            if rock - pre_rock < mid:
                del_rock += 1
            else:
                pre_rock = rock

        if del_rock > n:
            right = mid - 1
        else:
            answer = mid
            left = mid + 1

    return answer

print(solution(25,[2, 14, 11, 21, 17],2))