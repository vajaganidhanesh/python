set_1={1,2,3,2,1,1,2,1}
# print(set_1)
# print(type(set_1))
set_2 = {3,5,6}
# print(type(set_2))
# a = set_2.intersection(set_1)
# b = set_1.union(set_2)
# print(a)
# print(b)
# s = set()
# set_1.remove(1)
# print(set_1)
c = set_1.difference(set_2)
print(c)
d = set_1 - set_2
print(d)
s1 = {1,2,3,'a'}
s2 = {'a','b','c'}
s1.update(s2)
print(s1)
# we can increase & decrease the size of the set
s = {10,20,30}
s.add(302)
s.remove(302)
print(s)
print(s1.issuperset(s2))
print(s2.issubset(s2))