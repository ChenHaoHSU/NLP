import sys, os
import math
import numpy as np


##########################
# Problem Settings
##########################

def get_init_interval():
    return 0, 5

def target_range():
    return 0.01

def func(x):
    return (6 * math.exp(-2 * x)) + (2 * x * x)

##########################
# Solvers
##########################

def dichotomous():
    epsilon = 0.001
    a_init, b_init = get_init_interval()
    a_history, b_history = [a_init], [b_init]

    while b_history[-1] - a_history[-1] >= target_range():
        a_k, b_k = a_history[-1], b_history[-1]
        lumbda = ((a_k + b_k) / 2) - epsilon
        mu = ((a_k + b_k) / 2) + epsilon
        if func(lumbda) < func(mu):
            a_history.append(a_k)
            b_history.append(mu)
        else:
            a_history.append(lumbda)
            b_history.append(b_k)
    return a_history[-1], b_history[-1] 

##########################
# Main
##########################

def main():
    solver = dichotomous
    answer = solver()
    print('answer:',answer)

if __name__ == '__main__':
    print(math.exp(1))    
    main()
