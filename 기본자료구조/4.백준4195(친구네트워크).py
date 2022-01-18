# https://www.acmicpc.net/problem/4195
# 제한시간 20분~ 40분

# 결국 혼자 해결 못하고 답 보고 외움..

def find(x):
    if x == friends[x]:
        return x
    else:
        d = find(friends[x])
        friends[x] = d
        return friends[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        friends[y] = x
        number[x] += number[y]

n = int(input())

for _ in range(n):
    friends = dict()
    number = dict()

    f = int(input())

    for _ in range(f):
        x, y = input().split(' ')

        if x not in friends:
            friends[x] = x
            number[x] = 1
        if y not in friends:
            friends[y] = y
            number[y] = 1

        union(x,y)
        print(number[find(x)])