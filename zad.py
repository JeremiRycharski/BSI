import math
import numpy as np
def reliability_const_fail():
    """This is a function that allows calculating the reliability with the given failure rate and operational time, entering them one by one in the console.

    Returns:
        [type]: [description]
    """
    const_fail, time =[float(x) for x in input("Enter constant failure rate and time: ").split(" ")]  
    return "Reliability is {}".format('{:.10f}'.format(math.exp((-1)*const_fail*time)))

def highest_failure_rate():
    """This is a function that calculates the highest failure rate for a product, when given the reliability and time.
    
    

    Returns:
        [type]: [description]
    """
    reliability, time =[float(x) for x in input("Enter reliability and time: ").split(" ")]
    return "The highest failure rate is {}".format('{:.10f}'.format(np.log(reliability)/time))

def mtbf_failure_rate():
    """mtbf_failure_rate [summary]

    Returns:
        [type]: [description]
    """
    mtbf = float(input("Enter mtbf: "))
    return float('{:.4f}'.format(1/mtbf))

def item_reliability():
    """This is a function that achieves the correct mathematical formula for a reliability function when only MTBF is  given. Then, in the second step, by giving time (t), we are able to calculate the reliability of a given item.

    Returns:
        [type]: [description]
    """
    fail_rate = mtbf_failure_rate()
    print("R(t)=e^-({}*t)".format(fail_rate))
    time = float(input("Enter time: "))
    return '{:.10f}'.format(math.exp((-1)*fail_rate*time))

def probability_without_fail():
    """This is a function that calculates the probability of a given equipment failing in a given time by percentage. The user must provide the failure rate and the time of operating the equipment in the console.

    Returns:
        [type]: [description]
    """
    fail_rate = mtbf_failure_rate()
    time = float(input("Enter time: "))
    return "The probability of the equipment operating for {} hours without failure is {}".format(time, '{:.0%}'.format(math.exp((-1)*fail_rate*time)))

def units_fail_in_year(fail_rate, unit_amount, years):
    chosen_year = int(input("Enter year you chose: "))
    while chosen_year < 1 and chosen_year > years:
        chosen_year = int(input("Enter year you chose: "))
    
    for i in range(int(years)):
        if i == (chosen_year-1):
            fail_chosen_year = unit_amount*fail_rate
            
        unit_amount -= (unit_amount*fail_rate)
        
    return fail_chosen_year, chosen_year  

def remaining_units():
    fail_rate, unit_amount, years = [float(x) for x in input("Enter constant failure rate, number of units and number of years: ").split(" ")]  
    initial_unit_amount = unit_amount
    for i in range(int(years)):
        unit_amount -= (unit_amount*fail_rate)
    
    fail_chosen_year, chosen_year = units_fail_in_year(fail_rate, initial_unit_amount, years)
    return "After {} years {} will still be in service.\n{} will fail in year {}".format(years, int(unit_amount),       fail_chosen_year, chosen_year)

def choose_function(arg):
    return {
        '1': reliability_const_fail,
        '2': highest_failure_rate,
        '3': item_reliability,
        '4': probability_without_fail,
        '5': remaining_units,
    }[arg]()

print(choose_function(input("Choose function: ")))