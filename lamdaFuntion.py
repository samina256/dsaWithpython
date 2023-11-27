def appl(fx,value):
    return 6+fx(value)
double = lambda x: x*2
print(appl(lambda x : x*x,2))
print(double(5))