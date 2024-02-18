n = 20
a = 2
b =1 
drunk_coke = 0
remain_coke = 0
while True:
    n = (n // a) + b
    remain_coke = n % a
    drunk_coke +=n
    drunk_coke += remain_coke
    if n <=a :
        break
print(drunk_coke)