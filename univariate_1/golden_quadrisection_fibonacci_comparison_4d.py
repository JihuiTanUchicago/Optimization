from quadrisection_search_4a import algorithm_A
from golden_section_search_4b import algorithm_B
from fibonacci_search_4c import algorithm_C
import math
import inspect

def f1(x):
    return x * (x-5*math.pi)
def f2(x):
    return x + (4/x)
def f3(x):
    return - math.pow(x, 2) * math.sin(x)
def f4(x):
    return (-1)/math.pow(x-1,2) * (math.log(x) - 2*(x-1)/(x+1))

def compare_algorithms(f, interval, tolerance):
    print("====================BEGIN EVALUATION====================")
    print(f"|----------Evaluating Following Function----------------|")
    print(inspect.getsource(f))
    print(f"|**********Algorithm A (Quadrisection Search)***********|")
    algorithm_A(f=f, interval=interval, tolerance=tolerance)
    print(f"|**********Algorithm B (Golden Section Search)**********|")
    algorithm_B(f=f, interval=interval, tolerance=tolerance)
    print(f"|**********Algorithm C (Fibonacci Search)***************|")
    algorithm_C(f=f, interval=interval, tolerance=tolerance)
    print("======================END EVALUATION====================")
    print("\n\n")

compare_algorithms(f=f1, interval=[0,20], tolerance=1)
compare_algorithms(f=f2, interval=[0,2], tolerance=0.1)
compare_algorithms(f=f3, interval=[0, math.pi], tolerance=0.1)
compare_algorithms(f=f4, interval=[3/2, 9/2], tolerance=0.1)
                