x=[1,2,3,4,5,6,7]
y=[1,4,9,16,25,36,49]

init_index=1
end_index=5

h=(x[end_index]-x[init_index])/(end_index-init_index)

a = y[init_index]+y[end_index]
sum = 0
for i in range(init_index+1,end_index):
    sum=sum+y[i]

output = (h/2) * (a+2*(sum))

print(h)
print(a)
print(output)
