r = 1/12
epsilon = 1e-10
def apply_newton(x, r):
    return x * (2 - x * r)
def find_reciprocal(x_old, r, epsilon):
    print(f"x={x_old}, find reciprocal of {r}, tolerance: {epsilon}")
    x_new = apply_newton(x_old, r)
    while abs(x_new - x_old) > epsilon:
        x_old = x_new
        x_new = apply_newton(x_old, r)
        print(x_new)
    print(f"final answer: {x_new}")

find_reciprocal(0.1, r, epsilon)
find_reciprocal(1, r, epsilon)