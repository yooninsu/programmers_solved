number = 10
limit = 3
power = 2
knight = []
for i in range(1,number+1):
    divisor = []
    for j in range(1,int(i**(1/2)+1)):
        if i % j == 0:
            divisor.append(j)
            temp = []
            for k in divisor:
                temp.append(int(i/k))
    divisor = list(set(divisor+temp))
    if len(divisor) <= limit:
        knight.append(len(divisor))
    else:
        knight.append(power)
print(knight)