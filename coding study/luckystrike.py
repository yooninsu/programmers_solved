number =123402
def luckystraight(number):
    num = list(str(number))        
    temp1 = 0
    temp2 = 0
    for i in range(len(num))[:int(len(num)/2)]:
        temp1 += int(num[i])
    for j in range(len(num))[int(len(num)/2):]:
        temp2 += int(num[j])
    if temp1 == temp2:
        print('LUCKY')
    else:
        print('READY')
    
luckystraight(751234574321)