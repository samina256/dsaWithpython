a=9
print(id(a))
b=6
print(id(b))
c=5
print(id(c))
def someThing():
    a=13
    b=12
    c=10
    print(a,b,c)
    
    x=globals()['a']=24
    y=globals()['b']=45
    z=globals()['c']=30
    

someThing()
print(a,b,c)