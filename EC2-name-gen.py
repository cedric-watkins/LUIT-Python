'''Several departments share an AWS environment. You need to ensure that the EC2s
are properly named and are unique so team members can easily tell who the EC2
instances belong to. Use Python to create your unique EC2 names that the users
can then attach to the instances.'''
import random 
import string

#Prompt user to choose a department
print("Available Departments\nAccounting(acct), Marketing(mark), and FinOps(fin)\n")
department = input("Enter your Department (acct/mark/fin): ").lower()
N = 15 #number of characters to generate for instance id

while True:
    if department == "acct":
        print("Accounting")
        instance_id = ''.join(random.choices(string.ascii_lowercase +  string.digits, k = N))
        instances = int(input("\nHow many instances are you looking to run? "))
        print("")
        print("Your department EC2 names are:")
        for i in range(0, instances):
                print(department + "-" + str(instance_id))
        break
    
    elif department == "mark":
        print("Marketing")
        instance_id = ''.join(random.choices(string.ascii_lowercase +  string.digits, k = N))
        instances = int(input("\nHow many instances are you looking to run? "))
        print("")
        print("Your department EC2 names are:")
        for i in range(0, instances):
                print(department + "-" + str(instance_id))
        break
    
    elif department == "fin":
        print("FinOps")
        instance_id = ''.join(random.choices(string.ascii_lowercase +  string.digits, k = N))
        instances = int(input("\nHow many instances are you looking to run? "))
        print("")
        print("Your department EC2 names are:")
        for i in range(0, instances):
                print(department + "-" + str(instance_id))
        break
    
    else:
        print("\nEither Department does not exist or Invalid input.")
        break
