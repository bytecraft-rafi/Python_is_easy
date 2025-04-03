def fibo(num):
    if num <= 1:
        return num 
    else:
        return fibo(num-1) + fibo(num-2)

def print_fibonacci_series(n):
    for i in range(n):
        print(fibo(i), end=" ")

def sum_fibonacci_series(n):
    total = 0
    for i in range(n):
        total = total + fibo(i) 

    print(f"total sum till term {n}  is :", total)

num = int(input("Enter the number of terms: "))
print(f"Fibonacci series for {num} terms: ")
print_fibonacci_series(num)
print("\n")
sum_fibonacci_series(num)