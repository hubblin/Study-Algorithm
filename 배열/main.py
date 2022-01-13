# Q1 (https://programmers.co.kr/learn/courses/30/lessons/77484)

def check_score(n):
    print(n)
    for i in range(1, 7):
        if i == n:
            return 7 - i
    return 6


def solution(lottos, win_nums):
    answer = []

    win = len(set(lottos).intersection(win_nums))
    don_know = lottos.count(0)
    max_win = win + don_know
    min_win = win

    answer.append(check_score(max_win))
    answer.append(check_score(min_win))
    return answer


lottos = [0, 0, 0, 0, 0, 0]
win_nums = [38, 19, 20, 40, 15, 25]
answer = solution(lottos, win_nums)
print(answer)