def solution(numbers):
    numdict = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            sum_a = numbers[i]+numbers[j]
            numdict.add(sum_a)
    answer = list(numdict)
    print(sorted(answer))
numbers = [2,1,3,4,1]
solution(numbers)