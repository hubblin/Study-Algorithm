# 프로그래머스 https://programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    temp = -1
    for i in arr:
        if temp != i:
            answer.append(i)
            temp = i

    return answer


# arr = [1,1,3,3,0,1,1]
arr = [4, 4, 4, 3, 3]
answer = solution(arr)
print(answer)