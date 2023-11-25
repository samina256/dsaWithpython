# dic ={
#     265: "Samina",
#     299: "Sajjad",
#     231: "Hira",
#     278: "Rifat",
# }

# print(dic[265])     

info = {
    'name':'karan','age':24,'eligible':True
}  

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

print(info.items())
for item in info.items():
    print(f"the value corrosponding to the key is {item}")