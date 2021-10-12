arr = [1,'asf',123,1/2,0.123]
enum = list(enumerate(arr))
print(enum)
for index,values in enum:
    print("index:",index,"values:",values)