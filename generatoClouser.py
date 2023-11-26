#generator 
def gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
values = gen()
print(next(values))
print(next(values))

for i in values:
    print(i)

def gen():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
    
values=gen()
for i in values:
    print(i)
    

def gen():
    for i in range(10):
        yield i
    
values=gen()

for i in values:
    print(i)