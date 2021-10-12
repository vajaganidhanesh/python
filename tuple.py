array = (10,20,30)
# # print(type(array))
# # print(array[1])
# print(array)
# # for i in range(11,20,2):
# #     if(i%2==0):
# #         print(i)
# #     else:
# #         print(i)
# print(array.count)

# converting tuple to list by using loop and sequence:
tuple_to_list = list(array)
for i in ['a','b','c']:
    tuple_to_list.append(i)
print(tuple_to_list)
list_to_tuple = tuple(tuple_to_list)
print(list_to_tuple)