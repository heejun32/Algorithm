def solution(brown, yellow):
    total = brown + yellow

    # 카펫의 가로길이가 세로길이보다 크거나 같기 때문에 큰수에서 작은수로 반복
    for weight in range(total, 2, -1):  # 증가폭을 음수로 주면 마지막 값 + 1만큼 반복함
        if total % weight == 0:         # 카펫넓이에서 가로길이 탐색
            height = total // weight    # 카펫넓이 / 가로길이를 통해 세로길이 탐색

            # 구해진 카펫의 길이에서 테두리길이(2)만큼 빼주고 면적을 구한뒤 yellow의 면적과 같다면 해
            if yellow == (weight - 2) * (height - 2):
                return [weight, height]

print(solution(8, 1))

# 참고 사이트: https://coblin.xyz/35