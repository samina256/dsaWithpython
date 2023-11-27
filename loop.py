
# name ="samina"
# for i in name:
#     print(i,end=",\n")
# print("\n")  

# color = ["blue","Green","Red","black"]
# for i in color:
#     print(i)
#     for j in i:
#         print(j)
# print("\n") 

# for k in range(5):
#     print(k*5)
# print("\n")  

# for k in range(1,5):
#     print(k*5) 
# print("\n") 

# for k in range(1,9,2):
#     print(k*5) 
# print("\n") 

# i = int(input("Enter the number: "))
# while(i<=30):
#     i = int(input("Enter the number: "))
# print("done this loop")

# i = 5
# while (i>=0):
#     print(i)
#     i-=1
# print("i am inside the else")

# while True:
#     num = int(input("Do you want to comntinue?(yes/no)")).lower()
#     if num!= 'yes':
#         break


for i in range (101):
    if(i%2==0):
        pass
    elif(i==3):
        continue
    elif(i==99):
        break
    else:
        print(i)

print("done")