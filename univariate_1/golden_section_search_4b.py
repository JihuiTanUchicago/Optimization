import math

golden_ratio = (1+math.sqrt(5)) / 2
r = 1 / golden_ratio

def f(x):
    return x * math.sin(4*x)

def shrink(arr):
    a, b = arr
    x1 = b - r * (b-a)
    x2 = r * (b-a) + a
    f_x1 = f(x1)
    f_x2 = f(x2)
    if f_x1 <= f_x2:
        return [a, x2]
    else:
        return [x1, b]

def algorithm_B(tolerance, interval, f):
    print(f"local minimizor range {interval}: ", end='')
    iteration_count = 0
    while interval[1] - interval[0] > tolerance:
        interval = shrink(interval)
        iteration_count += 1
    x_star = (interval[0] + interval[1]) / 2
    print(f"x* = {x_star}, with local minimum is f(x*)= {f(x_star)}")

    print(f"Current Interval: {interval}")
    print(f"Number of iterations = {iteration_count}")

#algorithm_B(tolerance=1e-2, interval=[(7/8)*math.pi,3], f=f)

