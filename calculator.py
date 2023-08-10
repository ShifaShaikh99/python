import math
print("Select an operation to perform:")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Square Root")
print("6. Raise to power")
while True:
        operation=input("Enter choice(1,2,3,4,5,6):" )
        if operation =='1':
                        num1=input ("Enter first number: ")
                        num2=input("Enter second number: ")
                        print("The sum is "+ str(float(num1) + float(num2)) )
        elif operation =='2':
                        num1=input ("Enter first number: ")
                        num2=input("Enter second number: ")
                        print("The difference is "+ str(float(num1) - float(num2)) )
        elif operation =='3':
                        num1=input ("Enter first number: ")
                        num2=input("Enter second number: ")
                        print("The product is "+ str(float(num1) * float(num2)) )
        elif operation =='4':
                        num1=input ("Enter first number: ")
                        num2=input("Enter second number: ")
                        print("The result is "+ str(float(num1) / float(num2)) )
        elif operation =='5':
                        num=int(input ("Enter number: "))
                        print("The Squareroot is %f"  %(math.sqrt(num)))
        elif operation =='6':
                        num=int(input ("Enter number: "))
                        print("The result is %d" %(pow(num, 2 )))
        next_calculation=input("Lets do next calculation?(yes/no): ")
        if next_calculation== 'yes':
                continue
        else:
                break
