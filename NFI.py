import math

x = [1, 3, 5, 7]
y = [24, 120, 336, 720]

n = 8
h = x[1] - x[0]
p = (n - x[0]) / h
coeff = p
sum = y[0]
k = 1

for i in range(len(y) - 1, 0, -1):
    for j in range(i):
        y[j] = y[j + 1] - y[j]
    sum += coeff * y[0]
    coeff = coeff * (p - k) / (k + 1)
    k += 1

print(sum)
