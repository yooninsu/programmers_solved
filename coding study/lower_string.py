t = "3141592"
p = "271"
listt = list(t)
temp = []
answer = 0
while True:
    for i in range(len(listt)):
        if len(temp) == len(p):
            word = "".join(temp)
            print(word)
            if int(p) >= int(word):
                answer += 1
            temp.pop(0)
        elif len(temp) != len(p):
            temp.append(listt[i])
    break 