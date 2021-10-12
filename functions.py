# functions are used to particular tasks involved inside the project are any class
def greet():
    print("its all about function")
greet()

def multiple():
    n = int(input("enter the number:  "))
    limit = int(input("enter the limit: "))
    for i in range (1,limit+1):
            value = n*i
            print(f"{n} X {i} = {value}")
# multiple()

# functions with arguments
def multiple_arg(n1,limit1):
    for i in range(1,limit1+1):
        values = n1 * i
        print(f"{n1} X {i} = {values}")
multiple_arg(5,10)

# Functions using zip method as follows
numbers = [2,3,4,5,6,7]
limit = [10,10,10,10,10,10,10]
for numbers,limit in zip(numbers,limit):
    multiple_arg(n1=numbers,limit1=limit)
    # print("#"*10)

# Functions with arugments
def samplingproblem(a,b):
    c= a+b
    print(c)
samplingproblem(2,4)