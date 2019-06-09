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

def derivative(x):
    return ((-12) * math.exp(-2 * x)) + (4 * x)

def derivative2(x):
    return (24 * math.exp(-2 * x)) + 4

##########################
# Solvers
##########################

def dichotomous():
    print('Solved by dichotomous')
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

def golden():
    print('Solved by golden')
    alpha = 0.618
    a_init, b_init = get_init_interval()
    lumbda_init = a_init + ((1 - alpha) * (b_init - a_init))
    mu_init = a_init + (alpha * (b_init - a_init))
    a_history, b_history = [a_init], [b_init]
    lumbda_history, mu_history = [lumbda_init], [mu_init]

    while b_history[-1] - a_history[-1] >= target_range():
        a_k, b_k = a_history[-1], b_history[-1]
        assert len(a_history) == len(b_history)
        assert len(lumbda_history) == len(mu_history)
        if func(lumbda_history[-1]) > func(mu_history[-1]):
            a_history.append(lumbda_history[-1])
            b_history.append(b_history[-1])
            lumbda_history.append(mu_history[-1])
            mu_history.append(((1 - alpha) * a_history[-1]) + (alpha * b_history[-1]))
        else:
            a_history.append(a_history[-1])
            b_history.append(mu_history[-1])
            mu_history.append(lumbda_history[-1])
            lumbda_history.append((alpha * a_history[-1]) + ((1 - alpha) * b_history[-1]))
    return a_history[-1], b_history[-1]

def bisection():
    print('Solved by bisection')
    k = 1
    n = 100
    a_init, b_init = get_init_interval()
    a_history, b_history = [a_init], [b_init]
    while k <= n:
        k += 1
        lumbda_history = [(a_history[-1] + b_history[-1]) / 2]
        if derivative(lumbda_history[-1]) > 0:
            a_history.append(a_history[-1])
            b_history.append(lumbda_history[-1])
        else:
            a_history.append(lumbda_history[-1])
            b_history.append(b_history[-1])
    return a_history[-1], b_history[-1]

def newton():
    print('Solved by newton')
    lumbda_init = 1
    epsilon = 0.001
    lumbda_history = [lumbda_init]
    while True:
        if abs(derivative2(lumbda_history[-1])) < epsilon:
            break
        lumbda_current = lumbda_history[-1]
        lumbda_history.append(lumbda_current - (derivative(lumbda_current) / derivative2(lumbda_current)))
        if abs(lumbda_history[-1] - lumbda_history[-2]) < epsilon:
            break
    return lumbda_history[-1]

##########################
# Main
##########################

def main():
    solvers = [golden, dichotomous, bisection, newton]
    for solver in solvers:
        answer = solver()
        print('answer:',answer)

if __name__ == '__main__':
    print(math.exp(1))    
    main()
