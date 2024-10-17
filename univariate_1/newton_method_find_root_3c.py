import math

tolerance = 1e-3
def apply_newton(x):
    return x - (3 * math.sin(x)- 2 * x) / (3 * math.cos(x) - 2)

def find_root(x_old, tolerance):
    print(f"x={x_old}, find the (largest) root of y = 3sinx - 2x, tolerance: {tolerance}")
    x_new = apply_newton(x_old)
    while abs(x_new - x_old) > tolerance:
        x_old = x_new
        x_new = apply_newton(x_old)
        print(x_new)
    print(f"final answer: {x_new}")

find_root(2, tolerance)