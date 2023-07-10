s = 'baaab'   
s = list(s)
tmp = []
answer = []
for i in range(len(s)):
    if s[i] not in tmp:
        tmp.append(s[i])
        answer.append(-1)
    elif s[i] in tmp:
         for j in range(i-1,-1,-1):
                 if s[j] == s[i]:
                    num = i-j
                    answer.append(num)
                    break
print(answer)