def is_prime(num):
    flag = 0
    if num < 2 :
        flag = 1
    else :
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                flag = 1
                break
    return flag

def is_prime_inrange(start, end) :
    for i in range(start, end+1) :
        flag = (is_prime(i))

        if flag == 0:
            print(f"{i} is a prime number")

Start = int(input("Enter Starting range: "))
End = int(input("Enter Ending range: "))

is_prime_inrange(Start, End)