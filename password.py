import random
characters= "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789(){}[].,:;+_-\\/@#$&*!"
while True:
    pass_length=int(input("Enter the length of password: "))
    pass_count=int(input("Enter the number of passwords: "))
    for i in range(0, pass_count):
        password= ""
        for j in range(0, pass_length):
            pass_char= random.choice(characters)
            password= password+pass_char
        print("The generated password is: ",password)
    repeat=input("Do you want to generate more password? ")
    if repeat=="no" or repeat=="No":
        break
