t ="3141592"
p = "271"
listt = list(t)
print(listt)
temp = []
word = ""
count = 0
answer = 0
for a in listt:
    if count == len(p):
        word = "".join(temp)
        print(temp)
        print(word)
        count = 0
    else: 
        temp.append(a)
        count += 1
print(answer)