# https://www.acmicpc.net/problem/1874

n = int(input())

answer = []
lists = []
count = 1
for _ in range(n):
    temp = int(input())

    while count <= temp:
        lists.append(count)
        count += 1
        answer.append('+')

    if lists[-1] == temp:
        answer.append('-')
        lists.pop()
    else:
        print('No')
        exit(0)

print('\n'.join(answer))