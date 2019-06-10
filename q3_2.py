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
    return (((x_1 + (x_2 ** 3))) ** 2) + \
           (2 * ((x_1 - x_2 - 4) ** 4))

def derivative(x):
    return ((-12) * math.exp(-2 * x)) + (4 * x)

def derivative2(x):
    return (24 * math.exp(-2 * x)) + 4

##########################
# fibonacci sequence
##########################

def get_n(l):
    ret = []
    # print('l=', l)
    for i in range(1000):
        if i == 0 or i == 1:
            ret.append(1)
        elif ret[-1] > l:
            return len(ret) - 1
        else:
            ret.append(ret[-1] + ret[-2])
    return ret

def fb_seq(n):
    ret = [0]
    for i in range(1,n+1):
        if i == 0 or i == 1:
            ret.append(1)
        else:
            ret.append(ret[-1] + ret[-2])
    return ret

##########################
# Solvers
##########################

def fibonacci():
    print('Solved by Fibonacci method')
    a_init, b_init = get_init_interval()
    n = get_n( (b_init - a_init) / target_range())
    # print(n)
    F = fb_seq(n)

    lumbda_init = a_init + ((F[n-2] / F[n]) * (b_init - a_init))
    mu_init = a_init + ((F[n-1] / F[n]) * (b_init - a_init))
    a_history, b_history = [a_init], [b_init]
    lumbda_history, mu_history = [lumbda_init], [mu_init]

    for k in range(n):
        if func(lumbda_history[-1]) > func(mu_history[-1]):
            a_history.append(lumbda_history[-1])
            b_history.append(b_history[-1])
            lumbda_history.append(mu_history[-1])
            mu_history.append(a_history[-1] + ((F[n-k-1] / F[n-k]) * (b_history[-1] - a_history[-1])))
        else:
            a_history.append(a_history[-1])
            b_history.append(mu_history[-1])
            mu_history.append(lumbda_history[-1])
            lumbda_history.append(a_history[-1] + ((F[n-k-2] / F[n-k]) * (b_history[-1] - a_history[-1])))
        if k == n-2:
            lumbda_history.append(lumbda_history[-1])
            mu_history.append(lumbda_history[-1] + target_range())
            if func(lumbda_history[-1]) > func(mu_history[-1]):
                a_history.append(lumbda_history[-1])
                b_history.append(b_history[-1])
            else:
                a_history.append(a_history[-1])
                b_history.append(mu_history[-1])
            break
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
    print('Minimum theta(lumbda): {:.7f} when lumbda = {:.4f}'.format( func((a_history[-1] + b_history[-1]) / 2 ), (a_history[-1] + b_history[-1]) / 2))
    return a_history[-1], b_history[-1]

##########################
# Main
##########################

def main():
    solvers = [fibonacci]
    for solver in solvers:
        answer = solver()
        print('answer:',answer)

if __name__ == '__main__':
    main()
