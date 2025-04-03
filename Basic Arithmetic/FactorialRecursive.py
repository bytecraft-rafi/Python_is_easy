# num = 4
# factorial = 1

# while num != 0:
#     factorial = factorial * num
#     num = num -1
    
# print(factorial)

#recursive approach

def factorial(number) :
    if number ==0 or number == 1:
        return 1
    else:
        return number * factorial(number-1)

number = int(input("Enter a number"))
print(f"Factorial of {number} is  {factorial(number)}")