#This project will allow users to create a list of AWS Services through user input.
#It will randomly delete 2 items from the list, and see if the user can guess which items where removed

#Request the user to Enter AWS Services into a list
services = []
print("!!!Let's make a list of AWS Services!!! \n")

while True:
    services.append(input("Enter an AWS Service: ").title())
    
    choice = input("How about another? (y/n): ")
    print("")
    if choice.lower() == 'n':
        break
print(" ")

#Print list of Services entered and the number of items in the list
print(" Your list consist of:\n" , services)

print("----------------------------------")
print(" Your list consist of:\n" , len(services), " AWS Services")
print(" ")

