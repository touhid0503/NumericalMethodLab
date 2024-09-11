def fun(x):
    return x**3-x-2

def bis(a,b,f):
    if f(a)*f(b)>0:
        return None

    c=a
    while abs(f(c))>0.001:
        c=(a+b)/2
        if f(c)==0:
            return c
        if f(a)*f(c)>0:
            a=c
        else:
            b=c
    
    return c

print(bis(1,2,fun))
print(bis(2,1,fun))
print(bis(2,3,fun))
print(bis(1,3,fun))