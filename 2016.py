a = 5
b = 24
def solution(a,b):
    dow = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    daylist = [31,29,31,30,31,30,31,31,30,31,30,31]
    temp =[]

    for i in range(a):
        temp.append(daylist[i])
        if i == a-1:
            count +=b
        else:
            count = sum(temp)
        
    for k in range(count):
        result = dow[k%7]
    return result 