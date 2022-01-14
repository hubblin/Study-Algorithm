#https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    tot = len(stages)
    r = []

    for i in range(1, N + 1):
        temp = stages.count(i)
        # zeroDivision 예방
        if tot == 0:
            fail = 0
        else:
            fail = temp / tot
        r.append([fail, i])
        tot -= temp

    answer = sorted(r, reverse=True, key=lambda x: x[0])
    answer = [i[1] for i in answer]
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
answer = solution(N, stages)
print(answer)