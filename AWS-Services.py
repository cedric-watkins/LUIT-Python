#This project will allow players to create a list of AWS Services through user input.
#It will randomly delete 2 items from the list, and see if the player can guess which items where removed

#Request the user to Enter AWS Services into a list
services = []
print("!!!LET'S PLAY A GAME!!! \n???How many AWS services do you know??? \n\n!!!Let's build a list and make a game of it!!!")

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
print("")

num = random.ranint(0,len(services))

