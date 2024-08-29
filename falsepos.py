def f(x):
    return x**3 - x - 2

def falsePositionMethod(x_a, x_b, f, tol=1e-6, max_iter=100):
    if f(x_a) * f(x_b) > 0:
        print("Select different values: f(x_a) and f(x_b) must have different signs.")
        return None
    
    for _ in range(max_iter):
        # Compute the false position
        c = (x_a * f(x_b) - x_b * f(x_a)) / (f(x_b) - f(x_a))
        
        # Check if the result is within tolerance
        if abs(f(c)) < tol:
            return c
        
        # Update the interval [x_a, x_b]
        if f(x_a) * f(c) < 0:
            x_b = c
        else:
            x_a = c
    
    print("Method did not converge within the maximum number of iterations.")
    return c 

# Example usage
print("Root in interval [2, 3]:", falsePositionMethod(2, 3, f))
print("Root in interval [1, 2]:", falsePositionMethod(1, 2, f))
