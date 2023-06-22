def solution(number):
    answer = []
    count = 0   
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            for k in range(j+1,len(number)):    
                 answer.append([number[i],number[j],number[k]])
    res = list((tuple(sorted(sub)) for sub in answer))
    for num in res:
        if sum(num) == 0:
            count +=1
    return count

