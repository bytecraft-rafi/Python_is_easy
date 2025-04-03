def is_prime(num):
    if num < 2 :
        print(f"{num} is not a prime number")
    else :
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                return f"{num} is not a Prime Number"
                break
    return f"{num} is a Prime Number"

number = int(input("Enter a number: "))
print(is_prime(number))