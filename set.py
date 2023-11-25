#union() & update

# s1 = {1,2,3,6}
# s2 = {7,8,9}
# print(s1.union(s2))
# print(s1.intersection(s2))
# s1.update(s2)
# print(s1,s2)

# set1 = {"USA", "Canada", "Mexico"}
# set2 = {"France", "USA", "Canada", "Germany", "Italy"}
# set3 = set1.intersection(set2)
# print(set3)
# set1.intersection_update(set2)
# print(set1)

set1 = {"USA", "Canada", "Mexico"}
set2 = {"France", "USA", "Canada", "Germany", "Italy","Mexico"}
set3 = set1.intersection(set2)
print(set3)
set1.intersection_update(set2)
print(set1)
set3 = set1.symmetric_difference(set2)
print(set3)
set4=set2.difference(set1)
print(set4)
print(set1.isdisjoint(set2))
print(set2.issuperset(set1))
print(set1.issubset(set2))
set2.add("Austrelia")
print(set2)
set1.update(set2)
print(set1)
# set1.remove("USA")
# print(set1)
# # set1.remove("India")
# # print(set1)
# set1.discard("USA")
# print(set1)
# item = set1.pop()
# print(set1)
# print(item)

# del set1
# print(set1)
# set1.clear()
# print(set1)

if "Canada" in set1:
    print("Yes")
else:
    print("No")

samina= set()
print(type(samina))

for i in set2:
    print(i)