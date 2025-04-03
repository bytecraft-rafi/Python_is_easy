#Write a Python program to convert Celsius to Fahrenheit or Fahrenheit to Celsius
# inp_var = input("Input 1 to convert Celsius to Fahrenheit\n"
#                 "Or input 2 to convert Fahrenheit to Celsius: ")

# if inp_var == "1":
#     celsius_temp = float(input("Input temperature in Celsius: "))  # Convert input to float
#     fahrenheit_temp = (celsius_temp * 9/5) + 32
#     print(f"Fahrenheit temperature: {fahrenheit_temp}°F")
# elif inp_var == "2":
#     fahrenheit_temp = float(input("Input temperature in Fahrenheit: "))  # Convert input to float
#     celsius_temp = (fahrenheit_temp - 32) * 5/9
#     print(f"Celsius temperature: {celsius_temp}°C")
# else:
#     print("Invalid input. Please input 1 or 2.")
    
    
    
    #using functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

inp_var = input("Input 1 to convert Celsius to Fahrenheit\n"
                "Or input 2 to convert Fahrenheit to Celsius: ")

if inp_var == "1":
    celsius_temp = float(input("Input temperature in Celsius: "))  # Convert input to float
    fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
    print(f"Fahrenheit temperature: {fahrenheit_temp}°F")
elif inp_var == "2":
    fahrenheit_temp = float(input("Input temperature in Fahrenheit: "))  # Convert input to float
    celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
    print(f"Celsius temperature: {celsius_temp}°C")
else:
    print("Invalid input. Please input 1 or 2.")