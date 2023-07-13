def solution(numbers):
    numdict = {}
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            sum_a = numbers[i]+numbers[j]
            numdict[sum_a]= 1
    answer = list(numdict.keys())
    print(sorted(answer))
numbers = [2,1,3,4,1]
solution(numbers)
