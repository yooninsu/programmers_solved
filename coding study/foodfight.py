food = [1,3,4,6]
def solution(food):
    temp =[]
    for i in range(1,len(food)):
        num = food[i] // 2
        for j in range(num):
            temp.append(i)
    temp.append(0)
    for i in range(len(food)-1,0,-1):
        num = food[i] // 2
        for j in range(num):
            temp.append(i)
    string = map(str,temp)
    answer = "".join(string)
    return answer