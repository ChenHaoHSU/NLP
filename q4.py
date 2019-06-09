import sys, os
import math
import numpy as np


##########################
# Problem Settings
##########################

def start():
    return 0, 0

##########################
# Solvers
##########################

def deepest():
    print('Solved by deepest')
    return 0

##########################
# Main
##########################

def main():
    solvers = [deepest]
    for solver in solvers:
        answer = solver()
        print('answer:',answer)

if __name__ == '__main__':
    main()
