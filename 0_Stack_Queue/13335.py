
''' 내 풀이 1번
import sys
input = sys.stdin.readline

n, w, L = list(map(int, input().split()))
weights = list(map(int, input().split()))

def solution(n, w, L, weights):
    bridge = [0] * w
    time = 0

    while(len(weights) > 0 or sum(bridge) > 0): #대기 트럭이 없고, 다리 위에 트럭이 한대도 없을 때 종료
        time += 1

        if (len(weights) == 0): # 대기 트럽이 없으면 다리에 있는 마지막 트럭을 움직인다.
            bridge.pop(0)
            bridge.append(0)
        else:
            if (sum(bridge) + weights[0] > L):
                if bridge[0] > 0:
                    bridge.pop(0)

                    if (sum(bridge) + weights[0] <= L):
                        bridge.append(weights.pop(0))
                    else:
                        bridge.append(0)
                else:
                    bridge.append(bridge.pop(0))
            else:
                if bridge[0] > 0:
                    bridge.pop(0)
                    bridge.append(weights.pop(0))
                else:
                    bridge.pop(0)
                    bridge.append(weights.pop(0))

    print(time)

solution(n, w, L, weights)
'''

import sys
input = sys.stdin.readline

n, bridge_len, max_weight = list(map(int, input().split()))
trucks = list(map(int, input().split()))

def solution(bridge_len, max_weight, trucks):
    bridge = [0] * bridge_len
    weight = 0
    time = 0


    while(len(bridge) > 0) :
        passed = bridge.pop(0)
        weight -= passed

        if (len(trucks) > 0):
           if (weight + trucks[0] <= max_weight):
               bridge.append(trucks[0])
               weight += trucks[0]
               trucks.pop(0)
           else:
               bridge.append(0)

        time += 1

        if (sum(bridge) == 0):
            break

    print(time)

solution(bridge_len, max_weight, trucks)