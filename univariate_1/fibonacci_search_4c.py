import math

fib_nums = []
fib_nums.append(0)
fib_nums.append(1)

def f(x):
    return x * math.sin(4*x)

def get_fib(n):
    try:
        return fib_nums[n]
    except IndexError:
        for i in range(len(fib_nums), n+1):
            fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
        return fib_nums[n]
def get_phi(n):
    return get_fib(n+1) / get_fib(n)
def get_r(interval, tolerance):
    dif = interval[1] - interval[0]
    i = 1
    while get_fib(i) * tolerance <= dif:
        i += 1
    return 1 / get_phi(i)

def shrink(arr, tolerance):
    a, b = arr
    r = get_r(arr, tolerance)
    x1 = b - r * (b-a)
    x2 = r * (b-a) + a
    f_x1 = f(x1)
    f_x2 = f(x2)
    if f_x1 <= f_x2:
        return [a, x2]
    else:
        return [x1, b]

def algorithm_C(tolerance, interval, f):
    print(f"local minimizor range {interval}: ", end='')
    iteration_count = 0
    while interval[1] - interval[0] > tolerance:
        interval = shrink(interval, tolerance)
        iteration_count += 1
    x_star = (interval[0] + interval[1]) / 2
    print(f"x* = {x_star}, with local minimum is f(x*)= {f(x_star)}")

    print(f"Current Interval: {interval}")
    print(f"Number of iterations = {iteration_count}")

#algorithm_C(tolerance=1e-2, interval=[(7/8)*math.pi,3], f=f)

