def addition(x,y):
    return x+y
result = addition(4,5)
print(f"the resultant value of x and y is: {result}")

def even_or_odd(n):
    for i in n:
        if(i%2==0):
            print("even")
        else:
            print("odd")
even_or_odd(3)