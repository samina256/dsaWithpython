# #generator 
# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
#     yield 5
# values = gen()
# print(next(values))
# print(next(values))

# for i in values:
#     print(i)

# def gen():
#     n=1
#     while n<=10:
#         sq=n*n
#         yield sq
#         n+=1
    
# values=gen()
# for i in values:
#     print(i)
    

# def gen():
#     for i in range(10):
#         yield i
    
# values=gen()

# for i in values:
#     print(i)

# #Nested Function
# def outer_function(x):
#     # This variable is local to the outer_function
#     outer_variable = x

#     def inner_function():
#         # Access outer_variable from the outer function
#         print("Inner function accessing outer_variable:", outer_variable)

#     def modify_outer_variable(new_value):
#         nonlocal outer_variable
#         outer_variable = new_value
#         print("Inner function modified outer_variable:", outer_variable)

#     inner_function()
#     modify_outer_variable(42)
#     inner_function()

# # Call the outer function
# outer_function(10)

# def outer_function(x):
#     outer_variable = x
#     def inner_function():
#         nonlocal outer_variable
#         outer_variable = 34
#         print("innerfuntion: outer_variable= ",outer_variable)
#     print("outerfuntion: outer_variable= ",outer_variable)
#     inner_function()
#     print("outerfuntion: outer_variable= ",outer_variable)
# outer_function(10)

# def counter_creator():
#     count = 0  # This variable is in the outer function's scope

#     def increment():
#         nonlocal count  # Use nonlocal to indicate we're modifying the outer variable
#         count += 1
#         print("Counter value:", count)

#     return increment  # Return the inner function as a closure

# # Create two separate counters
# counter1 = counter_creator()
# counter2 = counter_creator()

# # Use the counters
# counter1()  # Output: Counter value: 1
# counter1()  # Output: Counter value: 2

# counter2()  # Output: Counter value: 1

#making counter iterable

# def counter_creator():
#     count = 0  # This variable is in the outer function's scope

#     def increment():
#         nonlocal count  # Use nonlocal to indicate we're modifying the outer variable
#         count += 1
#         return count

#     return increment  # Return the inner function as a closure

# # Create two separate counters
# counter1 = counter_creator()
# counter2 = counter_creator()

# # Use the counters in a loop
# for _ in range(5):
#     print(counter1())  # Output: 1, 2, 3, 4, 5

# for _ in range(3):
#     print(counter2())  # Output: 1, 2, 3

#making closer
def sum():
    sum=0
    def inner_sum():
         nonlocal sum
         for i in range(5):
             sum+=i
         return sum
    return inner_sum

counter1 = sum()
counter2= sum()

print(counter1())

#making closer with generator
def sum():
    sum=0
    def inner_sum():
         nonlocal sum
         for i in range(5):
             sum+=i
             yield sum
    return inner_sum

counter1 = sum()
counter2= sum()  

for result in counter1():
    print(result)