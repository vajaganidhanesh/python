a = int(input("enter the value : "))
c = int(input("enter the value : "))
b = int(input("enter the value : "))
if(a>b and a>c):
    print(f"{a} is the greatest number")
elif(b>a and b>c):
    print(f"{b} is the greatest number")
elif(a==b and b==c):
    # f"{}"-->it called f function we can define as below
    print(f"{b} {c} {a} values are equal numbers")   
else:
    print(f"{c} is the greatest number")


# if inside if statment 
number  = 100
if(number==a):
    if(number%b):
        print(f"{a} and {b}")
    else:
        print(number)
else:
    print(f"{a} is not equal to the number")