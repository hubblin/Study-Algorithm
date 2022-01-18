# https://www.acmicpc.net/problem/5397
#<<BP<A>>Cd-
#ThIsIsS3Cr3t
n = int(input())

for i in range(n):
    l = list(input())
    stack = list()
    stack2 = list()
    for j in l:
        if j == '<':
            if len(stack) != 0: stack2.append(stack.pop())
        elif j == '>':
            if len(stack2) != 0: stack.append(stack2.pop())
        elif j == '-':
            if len(stack) != 0: stack.pop()
        else:
            stack.append(j)
    print(''.join(stack + stack2[::-1]))



