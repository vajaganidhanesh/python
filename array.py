array_1 = [1,2,3,4,5]
array_2 = array_1
print(array_2,array_1)
array_1[0] = 99
print(array_2,array_1)
array_3 = array_1.copy()
print(array_3)