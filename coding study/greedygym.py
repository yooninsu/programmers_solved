n = 5
lost = [4,2]
reserve = [3,5]
student = list(range(1,n+1))
answer = []
cant =[]
temp = []
lost = sorted(lost)
reserve = sorted(reserve)
for i in student:
    if i in lost and i in reserve:
        cant.append(i)


for j in range(len(student)):
   if student[j] in lost and student[j] not in cant:
        if student[j] != 1 and student[j-1] in reserve and  student[j-1] not in cant:
            answer.append(student[j-1])
            cant.append(student[j-1])
        elif student[j] !=n and student[j+1] in reserve and student[j+1] not in cant:
            answer.append(student[j+1])
            cant.append(student[j+1])
   else:
       answer.append(student[j])

for k in answer:
    if answer.count(k) > 2:
        answer.remove(k)
print(answer)
