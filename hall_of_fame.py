score = [10, 100, 20, 150, 1, 100, 200]

k = 3
def solution(k,score):
    temp = []
    answer = []
    for i in range(len(score)):
        temp.append(score[i])
        temp = sorted(temp,reverse=True)
        if len(temp) <= k :
            answer.append(temp[-1])
        else:
            temp.pop()
            answer.append(temp[-1])
    print(answer)
# solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])