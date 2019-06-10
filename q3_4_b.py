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
    # x == lumbda
    x1 = (0,0)
    d = (1,1)
    x_1 = x1[0] + (x * d[0])
    x_2 = x1[1] + (x * d[1])
    return ((x_1 + x_2 ** 3) ** 2) + \
           2 * ((x_1 - x_2 - 4) ** 4)

def derivative(x):
    x1 = (5,4)
    d = (-2,1)
    x_1 = x1[0] + (x * d[0])
    x_2 = x1[1] + (x * d[1])
    return 2 * (d[0] + 3 * ((x1[1] + x * d[1]) ** 2) * d[1])  * ((x_1 + (x_2 ** 3))) + \
           (8 * ((x_1 - x_2 - 4) ** 3) * (d[0] - d[1]))

def derivative2(x):
    return (24 * math.exp(-2 * x)) + 4

##########################
# Solvers
##########################

def bisection():
    print('Solved by bisection search method')
    k = 1
    n = 14
    a_init, b_init = get_init_interval()
    a_history, b_history = [a_init], [b_init]
    lumbda_history = []
    while k <= n:
        k += 1
        lumbda_history.append((a_history[-1] + b_history[-1]) / 2)
        if derivative(lumbda_history[-1]) > 0:
            a_history.append(a_history[-1])
            b_history.append(lumbda_history[-1])
        else:
            a_history.append(lumbda_history[-1])
            b_history.append(b_history[-1])
    print('{:>11} {:>12} {:>12} {:>12} {:>18}'.format(\
          'Iteration_k', 'a_k', 'b_k', 'lumbda_k', 'theta\'(lumbda_k)'))
    for i, (a, b) in enumerate(zip(a_history, b_history)):
        if i == len(a_history) - 1:
            print('{:>11} {:12.3f} {:12.3f} {:<6} {:<6}'.format(\
                i+1, a, b, '', '', '', ''))
        else:
            print('{:>11} {:12.3f} {:12.3f} {:12.3f} {:18.11} {:18.11}'.format(\
                i+1, a, b, lumbda_history[i], derivative(lumbda_history[i]), func(lumbda_history[i])))
    print('Answer:')
    print('Uncertainty interval: [{:.5f}, {:.5f}]'.format(a_history[-1], b_history[-1]))
    print('Minimum theta(lumbda): {:.7f} when lumbda = {:.7f}'.format( func((a_history[-1] + b_history[-1]) / 2 ), (a_history[-1] + b_history[-1]) / 2))
    return a_history[-1], b_history[-1]

##########################
# Main
##########################

def main():
    solvers = [bisection]
    for solver in solvers:
        answer = solver()
        print('answer:',answer)

if __name__ == '__main__':
    main()
