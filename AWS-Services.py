#This project will allow players to create a list of AWS Services through user input.
#It will randomly delete 2 items from the list, and see if the player can guess which items where removed
import random

#Environment Variables
services = []
service = []
num = 0 #Number of service given

print("!!!LET'S PLAY A GAME!!! \n???Can you name (5) AWS Services??? \n\n!!!Let's build a list and make a game of it!!!")

#Request user to enter 5 services
for i in range(0, 5):
   
    num += 1
    print("AWS Service", num)
    services.append(input().title())
    
print("")

#Print list of Services entered and the number of items in the list
print(" Your list consist of:\n", services)
print(" ")
print("Congrats, You were able to name" , len(services), " AWS Services")
print("")

#This code will randomly remove 2 items in the list and store them in a seperate list 
num = random.sample(range(0, 5), 2)

num1 = num[0]
num2 = num[1]

item1 = services.pop(num1)
item2 = services.pop(num2)

rm_items = []

rm_items.append(item1)
rm_items.append(item2)

print("Can you guess which two services we've removed?")

#Prompt user to enter before continuig
for i in range(0, 1):
    
    print(input('Press "Enter" to continue:'))

#Print remaining results
print("Woah how did these 2 get here lol: \n", rm_items)
print("How'd you do?")
print("")

print("These are your new list details take a look below:")

print("Your new list consist of: ", services)
print("")

print("Leaving", len(services), "remaining services")

print("!!!Thanks for playing, Have a nice day!!!")