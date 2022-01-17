# https://www.acmicpc.net/problem/1920


#5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
n = int(input())
list1 = set(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))

for i in list2:
    if i in list1:
        print(1)
    else:
        print(0)