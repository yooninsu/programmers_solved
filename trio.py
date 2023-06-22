number= [0, 0, 1, -1, 0]
total = 0
answer = []
count = 0
for i in range(len(number)):
    for j in range(i+1,len(number)):
        for k in range(j+1,len(number)):    
                answer.append([number[i],number[j],number[k]])
res = list((tuple(sorted(sub)) for sub in answer))
print(res)
for num in res:
    if sum(num) == 0:
        count +=1
print(count)