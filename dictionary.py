d = {'dhanesh':[1,2,3,4],'dhani':2}
# print(d)
keys = d.keys()
# print(keys)
values = d.values()
# print(values)
print("key values are: ",d['dhanesh'])
print(d.items())
g = d.get('dhanesh')
# print(g)

#  iteration by using loop statement
seq = list(d.items())
for key, value in seq:
     print("key: ",key,"values: ",values)

# copy method
d1  = {'key_1':[1,2,3,4],
      'key_2':"started remembering python",
      'key_3':[True]*2}
for i,j in d1.items():
     print(i,j)

d2 = d1.copy()
print(d2) 

# pop method in dictionary
# print("Pop value of the d2 dictionary: ",d2.pop('key_3'))
print("",d2.popitem())