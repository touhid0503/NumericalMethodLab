def f(x):
    return x**3 - x - 2


def df(x):
    return 3 * x - 1


def newtonraphson(x0, f, df, tol=1e-6, max_iter=100):

    x = x0

    for _ in range(max_iter):

        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Derivative is zero. No solution found.")
            return None

        x_n = x - fx / dfx

        if abs(x_n - x) < tol:
            return x_n

        x = x_n

    print("Method did not converge within the maximum number of iterations.")
    return x


print(newtonraphson(2, f, df))
