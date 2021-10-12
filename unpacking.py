arr = [1, 2, 3]
a = arr[0]
b = arr[1]
c = arr[2]
print(a,b,c)

array = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12],
    [13,14,15]
]
for index,(x,y,z) in enumerate(array):
        print("index: ",index,"X:",x,"Y:",y,"Z:",z)

#Need to combine two arrays as one 
arr_1 = [1,2,3,4,5]
arr_2 = ['a','b','c','d','e']
combine = []
for i in range(len(arr_1)):
    combine.append([arr_1[i],arr_2[i]])
print(combine)

#zip fuction is alternate for it.
def new_func(arr_1, arr_2):
    combine = list(zip(arr_1,arr_2))
    print(combine)

new_func(arr_1, arr_2)