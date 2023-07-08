#Control Flow

num1 = int(input("Enter Number:"))
num2 = int(input("Enter Number:"))
num3 = int(input("Enter Number:"))


if ( (num1>num2) and (num1>num3) ):
    print("Largest num is",num1)
elif ( (num2>num1) and (num2>num3) ):
    print("Largest num is", num2)
else:
    print("Largest num is", num3)
