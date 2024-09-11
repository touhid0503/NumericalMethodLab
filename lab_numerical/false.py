def fun(x):
    return x**3-x-2

def falseP(a,b,f):
    if f(a)*f(b)>0:
        return None

    for _ in range(100):
    
        c=(a*f(b)-b*f(a))/(f(b)-f(a))
        fc=f(c)
        if abs(fc)<0.001:
            return c
        if f(a)*fc>0:
            a=c
        else:
            b=c
    
    return c

print(falseP(1,2,fun))
print(falseP(2,1,fun))
print(falseP(2,3,fun))
print(falseP(1,3,fun))