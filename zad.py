import math
import numpy as np
def reliability_const_fail():
    const_fail, time =[float(x) for x in input("Enter constant failure rate and time: ").split(" ")]  
    return math.exp((-1)*const_fail*time)

def highest_failure_rate():
    reliability, time =[float(x) for x in input("Enter reliability and time: ").split(" ")]
    return np.log(reliability)/time

def choose_function(arg):
    return {
        '1': reliability_const_fail(),
        '2': highest_failure_rate(),
    }.get(arg, "Wrong choice")

choose_function(arg = input())