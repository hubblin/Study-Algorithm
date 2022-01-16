# https://www.acmicpc.net/problem/2920

# 오름차순과 내림차순을 구분할 수 있어야 하는 문제

song = list(map(int, input().split()))
temp = 0
for i in range(1, len(song)):
    if song[i] - song[i-1] == 1:
        temp += 1
    elif song[i] - song[i-1] == -1:
        temp -= 1

if temp == 7:
    print('ascending')
elif temp == -7:
    print('descending')
else:
    print('mixed')