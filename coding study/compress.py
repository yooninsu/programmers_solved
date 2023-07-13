s = "abcabccdcd"
num = range(1,len(s))
count = 1
answer = ""
temp=[]
total = []
for i in range(1,len(s)):
    for j in range(0, len(s)-i, i):
        if s[j] == s[j+i]:
            count +=1
            if count > 1 and s[j] == s[count-1]:
                temp.append(count)
                temp.extend(s[i-1:count]) 
                if count == len(s):
                    break
        else:
            count =1

print(temp)
