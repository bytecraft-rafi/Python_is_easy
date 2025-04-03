def amstrongNumber(num) :
    temp = num
    count = 0
    while temp != 0 :
        temp = temp // 10
        count = count +1

    amsNum = num
    amsSum = 0
    for i in range (count+1):
        amsSum = amsSum +((amsNum % 10)**count)
        amsNum = amsNum // 10 

    if amsSum == num :
        return 0
    else :
        return 1       


num = 9474

flag = amstrongNumber(num)
if flag == 0: 
    print(f"{num} is an amstrong number")
else:
    print(f"{num} is not an amstrong number")