# https://www.acmicpc.net/problem/16234

n,l,r = map(int, input().split())
#N x N 이차원 배열을 선언한다
a = [[0 for i in range(n)] for i in range(n)]
aCheck = [[0]*n for i in range(n)]

# 일단 들어온 값을 이차원 배열에 담아야 한다.
for i in range(n):
    data = input().split()
    for j in range(n):
        a[i][j] = int(data[j])


# for 문을 돌면서 오른쪽, 아래쪽으로 검사를 한 뒤, 각 값을 temp 에 저장한다.
check = True
count = 0
while(check):
    temp = list()
    check = False
    for i in range(n):
        for j in range(n):
            now = a[i][j]
            if j != n - 1:
                right = a[i][j+1]
            if i != n-1:
                bottom = a[i+1][j]
            if j != n -1 and l <= abs(right - now) and abs(right - now) <= r:
                if aCheck[i][j] == 0:
                    aCheck[i][j] = 1
                    check = True
                if aCheck[i][j+1] == 0:
                    aCheck[i][j+1] = 1
                    check = True
            if i != n -1 and l <= abs(bottom - now) and abs(bottom - now) <= r:
                if aCheck[i][j] ==0:
                    aCheck[i][j] = 1
                    check = True
                if aCheck[i+1][j] == 0:
                    aCheck[i+1][j] = 1
                    check = True

    if check:
        count += 1
        for i in range(n):
            bCheck = False
            for j in range(n):
                if aCheck[i][j] == 1:
                    temp.append(a[i][j])
                    if i != n-1 and aCheck[i+1][j] == 1:
                        bCheck = True

                    if i == n-1:
                        bCheck = True

            if not bCheck and len(temp):
                myTemp = sum(temp) // len(temp)
                temp = list()
                for x in range(i+1):
                    for y in range(n):
                        if aCheck[x][y] == 1:
                            a[x][y] = myTemp
                            aCheck[x][y] = 0

        if len(temp):
            m = sum(temp) // len(temp)
            for i in range(n):
                for j in range(n):
                    if aCheck[i][j] == 1:
                        aCheck[i][j] = 0
                        a[i][j] = m

print(count)