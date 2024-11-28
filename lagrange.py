x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]
n = float(input())
res = 0

for i in range(0, 6):
    m = 1
    k = 1
    for j in range(0, 6):
        if i != j:
            m = m * (n - x[j])
            k = k * (x[i] - x[j])
    res = res + (m / k) * y[i]

print(res)
