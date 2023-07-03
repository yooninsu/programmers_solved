s = 'K1KA5CB7'
def rearrange(s):
    answer = ''
    slist = list(s)
    numlist = ['1','2','3','4','5','6','7','8','9','0']
    tempStr = []
    tempInt = 0 
    for i in range(len(list(s))):
        if slist[i] in numlist:
            tempInt += int(slist[i])
            a = str(tempInt)
        else:
            tempStr.append(slist[i])
            tempStr.sort()
    tempStr.append(a)
    answer= ''.join(tempStr)
    print(answer)

rearrange(s)
rearrange('AJKDLSI412K4JSJ9D')