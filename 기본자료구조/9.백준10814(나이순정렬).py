# https://www.acmicpc.net/problem/10814
# 난이도 : 하
# 제한시간 : 20분

n = int(input())
array = []
for _ in range(n):
    a,b = input().split()
    array.append((int(a), b))

array = sorted(array, key=lambda x: x[0])

for i in array:
    print(i[0], i[1])
