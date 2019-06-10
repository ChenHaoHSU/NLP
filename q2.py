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
    print('Solved by dichotomous search method')
    epsilon = 0.001
    a_init, b_init = get_init_interval()
    a_history, b_history = [a_init], [b_init]
    lumbda_history, mu_history = [], []
    while b_history[-1] - a_history[-1] >= target_range():
        a_k, b_k = a_history[-1], b_history[-1]
        lumbda = ((a_k + b_k) / 2) - epsilon
        mu = ((a_k + b_k) / 2) + epsilon
        lumbda_history.append(lumbda)
        mu_history.append(mu)
        if func(lumbda) < func(mu):
            a_history.append(a_k)
            b_history.append(mu)
        else:
            a_history.append(lumbda)
            b_history.append(b_k)

    print('{:>11} {:>12} {:>12} {:>12} {:>12} {:>15} {:>12}'.format(\
          'Iteration_k', 'a_k', 'b_k', 'lumbda_k', 'mu_k', 'theta(lumbda_k)', 'theta(mu_k)'))
    for i, (a, b) in enumerate(zip(a_history, b_history)):
        if i == len(a_history) - 1:
            print('{:>11} {:12.3f} {:12.3f} {:<6} {:<6} {:<6} {:<6}'.format(\
                i+1, a, b, '', '', '', ''))
        else:
            print('{:>11} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:15.3f} {:12.3f}'.format(\
                i+1, a, b, lumbda_history[i], mu_history[i], func(lumbda_history[i]), func(mu_history[i])))
    print('Answer:')
    print('Uncertainty interval: [{:.5f}, {:.5f}]'.format(a_history[-1], b_history[-1]))
    print('Minimum: {:.7f}'.format( func((a_history[-1] + b_history[-1]) / 2 )))
    return a_history[-1], b_history[-1]

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
            print('{:>11} {:12.3f} {:12.3f} {:<6} {:<6} {:<6} {:<6}'.format(\
                i+1, a, b, '', '', '', ''))
        else:
            print('{:>11} {:12.3f} {:12.3f} {:12.3f} {:12.3f} {:15.3f} {:12.3f}'.format(\
                i+1, a, b, lumbda_history[i], mu_history[i], func(lumbda_history[i]), func(mu_history[i])))
    print('Answer:')
    print('Uncertainty interval: [{:.5f}, {:.5f}]'.format(a_history[-1], b_history[-1]))
    print('Minimum: {:.7f}'.format( func((a_history[-1] + b_history[-1]) / 2 )))
    return a_history[-1], b_history[-1]

def bisection():
    print('Solved by bisection search method')
    k = 1
    n = 39
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
    print('{:>11} {:>12} {:>12} {:>12} {:>16}'.format(\
          'Iteration_k', 'a_k', 'b_k', 'lumbda_k', 'theta\'(lumbda_k)'))
    for i, (a, b) in enumerate(zip(a_history, b_history)):
        if i == 6: print('...')
        if i >= 6 and i <= n - 6: continue
        if i == len(a_history) - 1:
            print('{:>11} {:12.3f} {:12.3f} {:<6} {:<6}'.format(\
                i+1, a, b, '', '', '', ''))
        else:
            print('{:>11} {:12.3f} {:12.3f} {:12.3f} {:16.10f}'.format(\
                i+1, a, b, lumbda_history[i], derivative(lumbda_history[i])))
    print('Answer:')
    print('Uncertainty interval: [{:.5f}, {:.5f}]'.format(a_history[-1], b_history[-1]))
    print('Minimum: {:.7f}'.format( func((a_history[-1] + b_history[-1]) / 2 )))
    return a_history[-1], b_history[-1]

def newton():
    print('Solved by Newton\'s method')
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
    print('{:>11} {:>12} {:>16} {:>17} {:>12}'.format(\
          'Iteration_k', 'lumbda_k', 'theta\'(lumbda_k)', 'theta\'\'(lumbda_k)',  'lumbda_(k+1)'))
    for i, lumbda in enumerate(lumbda_history):
        if i == len(lumbda_history) - 1: 
            continue
        else:
            print('{:>11} {:12.4f} {:16.4f} {:17.4f} {:12.4f}'.format(\
                i+1, lumbda, derivative(lumbda), derivative2(lumbda), lumbda_history[i+1]))
    print('Answer:')
    print('Minimum: {:.7f}'.format( func(lumbda_history[-1])))
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
    main()
