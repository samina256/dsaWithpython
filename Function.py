# def calculateGmean(a,b):
#     mean= (a*b)/(a+b)
#     print( mean)

# def isGreater(a,b):
#     if(a>b):
#         print('first one is greater')
#     else:
#         print('Second one is greater')
# a=7
# b=5
# isGreater(a,b)
# calculateGmean(a,b)

# c=4
# d=70
# isGreater(c,d)
# calculateGmean(c,d)

#default argument
#9,1 set as defargument

# def average(a=9,b=1):
#     print('the average is',(a+b)/2)

# average()
# average(b=9)
# average(2,3)

#keyword argument
#thr order of which argument pass doesn't matter
# average(b=3,a=6)

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#     print("Average is: ", sum/len(numbers))
    

# average(5,6,8,9,3,4,2)

#variable lenghth argumemnt

# def name(*num):
#     print('hello', num[0],num[1],num[2])

# name("peter","jon","ram")

# def name(**num):
#     print("hello",num["li"],num["lo"],num["lp"])

# name(li ="Samina",lo = "Sajjad",lp ="Sahin")

# def name(*num):
#     print(num)
# name(567,89,78,0)

# def person(name,**data):
#     print(name,data)
#     for i,j in data.items():
#        print(i,j)

# person('Samina',age=24,city='Mumbai',mob= 1778144803)

def doItAfter():
     pass