# Build a simple calculator that takes two numbers and an operator (+, -, *, /) as inputs and performs the operation.

import math 
while True:
    print(f"Choose option from the menu-")
    print(f"1 for Addition")
    print(f"2 for Subtraction")
    print(f"3 for Multiplication")
    print(f"4 for Division")
    print(f"5 for Quadrtic Equation")
    print(f"0 for exit")

    option = int(input("Option: "))

    if option == 1:
        num1= int(input("Enter first Number: "))
        num2= int(input("Enter second Number: "))
        result = num1+num2
        print("Result is: ", result)
    elif option ==2 :
        num1= int(input("Enter first Number: "))
        num2= int(input("Enter second Number: "))
        if num1 >= num2 :
            result = num1-num2 
            print(f"Result is: ", result)
        else :
            result = num2-num1
            print(f"Result is: ", result)
    elif option == 3:
        num1= int(input("Enter first Number: "))
        num2= int(input("Enter second Number: "))
        result = num1*num2
        print(f"Result is: ", result)
    elif option == 4:
        num1= int(input("Enter first Number: "))
        num2= int(input("Enter second Number: "))
        if num2 != 0:
            result = float(num1/num2)
            print(f"Result is: ", result)
        elif num2 ==0:
            print(f"Divisor can not be zero")
    elif option == 5:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        if a == 0:
            print(f"coefficient of a can not be zero")
        else :
            discriminant = b**2 -4*a*c
            if  discriminant > 0:
                print(f"two real roots")
                root1 = (-b + math.sqrt(discriminant))/ (2*a)
                root2 = (-b - math.sqrt(discriminant))/ (2*a)
                print(f"roots are : ", root1, root2)
            elif discriminant == 0:
                root = (-b)/(2*a)
                print(f"One repeated real root")
                print(f"repeated root is : ", root)
            elif discriminant < 0:
                print(f"two complex roots")
                root_real = (-b)/(2*a)
                root_imgn = (math.sqrt(abs(discriminant)))/(2*a)
                # print(f"root 1 : ",root_real ,"+",root_imgn,"i")
                # print(f"root 2 : ",root_real ,"-",root_imgn,"i")
                print(f"Root 1: {root_real}+{root_imgn}i")
                print(f"Root 2: {root_real}-{root_imgn}i")
                
    elif option == 0 or option not in (1, 2, 3, 4, 5) :
        print(f"exiting calculator")
        break
    
 