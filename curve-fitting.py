# Number of data points
n = 5

# Predefined values of x and y
x = [1, 2, 3, 4, 5]
y = [0.6, 2.4, 3.5, 4.8, 5.7]

# Initialize sums
sumx = 0
sumy = 0
sumxy = 0
sumx2 = 0

# Calculate sums using a for loop
for i in range(n):
    sumx += x[i]
    sumy += y[i]
    sumxy += x[i] * y[i]
    sumx2 += x[i] ** 2

# Calculate slope (a) and intercept (b) for the line y = ax + b
a = (n * sumxy - sumx * sumy) / (n * sumx2 - sumx ** 2)
b = (sumy - a * sumx) / n

print(f"The best fit line is: y = {a:.2f}x + {b:.2f}")
