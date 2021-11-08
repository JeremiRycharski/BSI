import math
import numpy as np


#zad 03.01
def reliability_const_fail():
    const_fail, time =[float(x) for x in input("Enter constant failure rate and time: ").split(" ")]  
    return math.exp((-1)*const_fail*time)

#zad 04.01
def highest_failure_rate():
    reliability, time =[float(x) for x in input("Enter reliability and time: ").split(" ")]
    return np.log(reliability)/time

#zad 05a.01
def reliability_function():
    MTBF,t =[float(x) for x in input("Enter mean time between failures(MTBF): ")]
    return ' λ = ', 1 / MTBF, '\ntherefore the reliability function is given by: \n', math.exp((-1) * MTBF * t)
    

#zad 05b.01
#def reliability_of_the_item():

print("Lol")