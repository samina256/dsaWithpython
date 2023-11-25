# dic ={
#     265: "Samina",
#     299: "Sajjad",
#     231: "Hira",
#     278: "Rifat",
# }

# print(dic[265])     

# info = {
#     'name':'karan','age':24,'eligible':True
# }  

# print(info)
# # print(info['name2'])
# print(info['name'])
# print(info.get('name2'))

#key() method
# print(info.keys())
# print(info.values())

# for key in info.keys():
#     print(f"the value corrosponding to the key {key} is {info[key]}")

#item()method

# print(info.items())
# for key,value in info.items():
#     print(f"the value corrosponding to the key{key} is {value}")


#dictionary methods
# ep1 = {122:46, 123:46,567:89,670:90,90:12,34:45,23:65}
# ep2 = {35:67,67:98}

# #update()
# ep1.update(ep2)
# print(ep1)

# #clear()
# ep2.clear()
# print("this is ep2: ",ep2)

# #empty
# empty = {}
# print(empty)

# #pop()
# ep1.pop(122)
# print(ep1)

# #popitem()
# ep1.popitem()

# #del
# # del ep1
# del ep1[123]
# print(ep1)

#list(dictionary)
# ep1[479]=77
# print(ep1)
# print(list(ep1))
# list(ep1)
# print(sorted(ep1))

dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

#adding two loop to make dictionary
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

print(type(questions))

que= ['name','id','grade']
ans= ['Samina',265,3.50]
for q,a in zip(que,ans):
    print('what is your{0}? it\'s {1}' .format(q,a))