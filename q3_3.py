import sys, os
import math
import numpy as np


##########################
# Problem Settings
##########################

def get_init_interval():
    return -2, 2

def target_range():
    return 0.01

def func(x):
    # x == lumbda
    x1 = (5,4)
    d = (-2,1)
    x_1 = x1[0] + (x * d[0])
    x_2 = x1[1] + (x * d[1])
    return (((x_1 + (x_2 ** 3))) ** 2) + \
           (2 * ((x_1 - x_2 - 4) ** 4))

##########################
# Solvers
##########################

def golden():
    print('Solved by golden section method')
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
    print('{:>11} {:>12} {:>12} {:>12} {:>12} {:>15} {:>12}'.format(\
          'Iteration_k', 'a_k', 'b_k', 'lumbda_k', 'mu_k', 'theta(lumbda_k)', 'theta(mu_k)'))
    for i, (a, b) in enumerate(zip(a_history, b_history)):
        if i == len(a_history) - 1:
            print('{:>11} {:12.6f} {:12.6f} {:<6} {:<6} {:<6} {:<6}'.format(\
                i+1, a, b, '', '', '', ''))
        else:
            print('{:>11} {:12.6f} {:12.6f} {:12.6f} {:12.6f} {:15.6f} {:12.6f}'.format(\
                i+1, a, b, lumbda_history[i], mu_history[i], func(lumbda_history[i]), func(mu_history[i])))
    print('Answer:')
    print('Uncertainty interval: [{:.5f}, {:.5f}]'.format(a_history[-1], b_history[-1]))
    print('Minimum theta(lumbda): {:.7f} when lumbda = {:.7f}'.format( func((a_history[-1] + b_history[-1]) / 2 ), (a_history[-1] + b_history[-1]) / 2))
    return a_history[-1], b_history[-1]

##########################
# Main
##########################

def main():
    solvers = [golden]
    for solver in solvers:
        answer = solver()
        print('answer:',answer)

if __name__ == '__main__':
    main()
