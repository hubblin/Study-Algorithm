# https://www.acmicpc.net/problem/2798

# 완전탐색 난이도 Very easy

n, m = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0
for i in range(len(cards)):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            result = cards[i] + cards[j] + cards[k]
            if result <= m and result > answer:
                answer = result

print(answer)