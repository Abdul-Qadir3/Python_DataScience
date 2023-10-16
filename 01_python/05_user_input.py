# name =input("Enter your name : ") #user input

# print("Hello Mr: ", name, ", How are you") #output

#==============================================================

person_A_name = input("Please input your name : ")
person_A_age=int(input("How old are u? "))

person_B_name = input("Please input your name : ")
person_B_age=int(input("How old are u? "))

if person_A_age>person_B_age:
    print(person_A_name, "is older then ", person_B_name)
else:
    print(person_A_name, "is younger then ", person_B_name)