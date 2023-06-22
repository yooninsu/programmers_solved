number = 1000
limit = 30
power =2
knight = []
count = 0
for i in range(1,number+1):
    count = 0
    for j in range(1,int(i+1/2)):
        if i % j == 0:
            count += 1    
    if count <= limit:
        knight.append(count)
    else:
        knight.append(power)
print(knight)