#Determine if a inserted range of numbers are divisible by 3 and/or 5
my_range = int(input("How many number should we process? "))

for i in range(1, my_range + 1):
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
        
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        