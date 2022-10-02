#This Code will Convert Fahrenheit(User input) to Celsius.

F = float(input("What temperature(in Fahrenheit) would you like converted(to Celsius)? "))
C = (F - 32) * 5 / 9
print(F, "F is" , round(C,2) , "C")

