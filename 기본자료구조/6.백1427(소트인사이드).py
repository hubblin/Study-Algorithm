# https://www.acmicpc.net/problem/1427

s = input()
n = [int(i) for i in s]

n.sort(reverse=True)

print(''.join([str(i) for i in n]))