# def f(x):
#     return x**3-x-2

# def bisectionMethod(x_a,x_b,f):
#     if f(x_a)*f(x_b)>0:
#         print("select different values")
#     c=x_a
#     while abs(f(c)-0)>0.001:
#         c=x_a+x_b/2
#         if f(c)==0:
#             return c
#         if f(x_a)*f(x_b)>0:
#             x_a=c
#         else:
#             x_b=c
#     return c

        
    
# print(bisectionMethod(2,3,f))
# print(bisectionMethod(1,2,f))
def f(x):
    return x**3 - x - 2

def bisectionMethod(x_a, x_b, f):
    if f(x_a) * f(x_b) > 0:
        print("Select different values")
        return None
    
    c = x_a
    while abs(f(c)) > 0.001:
        c = (x_a + x_b) / 2
        if f(c) == 0:
            return c
        if f(x_a) * f(c) > 0:
            x_a = c
        else:
            x_b = c
    
    return c

print(bisectionMethod(2, 3, f))
print(bisectionMethod(1,2,f))

