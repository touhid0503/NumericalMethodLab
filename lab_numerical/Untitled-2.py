def false_position_method(a, b, f, tol=0.001, max_iter=100):
    """
    Find the root of the function f(x) in the interval [a, b] using the False Position method.
    
    Parameters:
    - a: lower bound of the interval
    - b: upper bound of the interval
    - f: function for which we want to find the root
    - tol: tolerance for convergence (default is 0.001)
    - max_iter: maximum number of iterations (default is 100)
    
    Returns:
    - The approximate root within the interval [a, b] if found, else None.
    """
    if f(a) * f(b) > 0:
        print("Function values at the endpoints must be of opposite signs.")
        return None
    
    for _ in range(max_iter):
        # Compute the false position (interpolation point)
        c = b - (f(b) * (a - b)) / (f(a) - f(b))
        fc = f(c)
        
        # Check for convergence
        if abs(fc) < tol:
            return c
        
        # Update the interval based on the sign of f(c)
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    return c

# Example usage:
def fun(x):
    return x**3 - x - 2

root = false_position_method(1, 2, fun)
print(f"The root is approximately: {root}")
