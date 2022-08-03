from collections import defaultdict


def solution(id_list, report, k):
    answer = []
    
    report_dict = defaultdict(set)
    reported_dict = defaultdict(set)
    for r in report:
        user, reported_user = r.split()
        report_dict[user].add(reported_user)
        reported_dict[reported_user].add(user)

    for user_id in id_list:
        count = 0
        for reported_user in report_dict[user_id]:
            if len(reported_dict[reported_user]) >= k:
                count += 1
        answer.append(count)

    return answer