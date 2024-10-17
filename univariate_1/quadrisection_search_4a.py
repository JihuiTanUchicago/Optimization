import math

def f(x):
    return x * math.sin(4*x)
def get_equal_intervals(arr, num): #arr = [a, b], indicating an interval
    a, b = arr
    length = (b-a) / num
    results = []
    for i in range(num):
        results.append([a+length*i, a+length*(i+1)])
    return results
def get_interior_points(intervals): #directly associated with get_four_equal_intervals
    interior_points = []
    for i in range(0, len(intervals)-1):
        interior_points.append(intervals[i][1])
    return interior_points
def shrink(arr,num):
    intervals = get_equal_intervals(arr,num)
    interior_points = get_interior_points(intervals)
    f_points = []
    for point in interior_points:
        f_points.append(f(point))
    _, min_index = min((val, idx) for idx, val in enumerate(f_points))
    new_interval = [intervals[min_index][0], intervals[min_index+1][1]]
    return new_interval

def algorithm_A(tolerance, interval, f, sub_interval_num=4):
    print(f"local minimizor range {interval}: ", end='')
    iteration_count = 0
    while interval[1] - interval[0] > tolerance:
        interval = shrink(interval, sub_interval_num)
        iteration_count += 1
    x_star = sum(interval)/len(interval)
    print(f"x* = {x_star}, with local minimum is f(x*)= {f(x_star)}")

    print(f"Current Interval: {interval}")
    print(f"Number of iterations = {iteration_count}")

#algorithm_A(tolerance=1e-2, interval=[(7/8)*math.pi,3],sub_interval_num=4, f = f)

