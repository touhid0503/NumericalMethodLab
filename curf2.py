import numpy as np

# Number of data points
n = 5

# Predefined values of x and y
x = [1.0, 3.0, 5.0, 7.0, 9.0]
y = [2.473, 6.722, 18.274, 49.673, 135.029]

# Initialize log_y list
log_y = []

# Calculate the logarithm of each y value
for i in range(n):
    log_y.append(np.log(y[i]))

# Initialize sums
sumx = 0
sum_log_y = 0
sumxy = 0
sumx2 = 0

# Calculate sums using a for loop
for i in range(n):
    sumx += x[i]
    sum_log_y += log_y[i]
    sumxy += x[i] * log_y[i]
    sumx2 += x[i] ** 2

# Calculate slope (b) and intercept (A)
b = (n * sumxy - sumx * sum_log_y) / (n * sumx2 - sumx ** 2)
A = (sum_log_y - b * sumx) / n

# Calculate a from A
a = np.exp(A)

print(f"The best fit exponential function is: y = {a:.4f} * e^({b:.4f} * x)")
