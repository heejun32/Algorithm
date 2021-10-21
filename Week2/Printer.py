priorities = list(input())
location = int(input())

def solution(priorities, location):
    loc = [i for i in range(len(priorities))]
    sort_loc = []

    while(len(priorities) > 0):
        if priorities[0] < max(priorities):
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
        else:
            priorities.pop(0)
            sort_loc.append(loc.pop(0))

    answer = sort_loc.index(location) + 1
    return answer

# https://mong9data.tistory.com/29
# 기존에 큐로 접근하는 방식은 맞았지만, location 을 찾을 수 있는 방법은 어렵게 생각함
# 문제 접근에 있어 기존 방법을 활용하는 방식으로 코딩해볼 것.