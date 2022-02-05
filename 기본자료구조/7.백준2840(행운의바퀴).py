# https://www.acmicpc.net/problem/2840
import sys
n, k = map(int, input().split())

result = ['?']*n
point = 0

for _ in range(k):
    s, p = input().split()
    s = int(s)

    point -= s
    point %= n
    if p in result and result[point] != p:
        print("!")
        sys.exit()
    elif result[point] != '?' and result[point] != p:
        print("!")
        sys.exit()
    else:
        result[point] = p
temp = ""
for _ in range(n):
    temp += result[point]
    point = (point + 1) % n

print(temp)