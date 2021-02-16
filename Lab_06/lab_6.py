from math import *
import numpy as np
import matplotlib.pyplot as plt
def init():
    x = [1, 2, 3, 4, 5, 6]
    y = [0.571, 0.889, 1.091, 1.231, 1.333, 1.412]
    return x, y
def rightDiffDerivative(y, h, i):
    return (y[i+h] - y[i]) / h
def leftDiffDerivative(y, h, i):
    return (y[i] - y[i-h]) / h
def centerDiffDerivative(y, h, i):
    n = len(y)-1
    if i == 0:
        return (-3*y[0] + 4*y[1] - y[2]) / (2*h)
    if i == n:
        return (3*y[n] - 4*y[n-1] + y[n-2]) / (2*h)
    return (y[i+1] - y[i-1]) / (2*h)
#Рунге с использованием односторонней производной,
# p = 1
# m = 2
def runge(y, i):
    if (i < len(y) - 2):
        f1 = rightDiffDerivative(y, 1, i)
        f2 = rightDiffDerivative(y, 2 ,i)
        return f1 + (f1-f2)
    f1 = leftDiffDerivative(y, 1, i)
    f2 = leftDiffDerivative(y, 2, i)
    return f1 + (f1-f2)

#xi = 1/x
#eta = 1/y
def flatteningPara(x, y, i):
    tmp = i+1
    if i == len(y) - 1:
        tmp = i-1
    f1 = (1/y[tmp] - 1/y[i]) / (1/x[tmp] - 1/x[i])
    f2 = y[i]**2 / x[i]**2
    return f1*f2

def secondDerivative(y, h, i):
    n = len(y)-1
    if i == 0:
        return (y[0] - 2*y[1] + y[2]) / h**2
    if i == n:
        return (y[n] - 2*y[n-1] + y[n-2]) / h**2
    return (y[i-1] - 2*y[i] + y[i+1]) / h**2

def main():
    x, y = init();
    print(("{:>10}"*7).format("a", "b", "1", "2", "3", "4", "5"))
    for i in range(0, 6):
        print("{:10.3f}".format(x[i]), end="")
        print("{:10.3f}".format(y[i]), end="")
        if (i == 5):
            print("{:10.3f}".format(leftDiffDerivative(y, 1, i)), end="")
        else:
            print("{:10.3f}".format(rightDiffDerivative(y, 1, i)), end="")
        print("{:10.3f}".format(centerDiffDerivative(y, 1, i)), end="")
        print("{:10.3f}".format(runge(y, i)), end="")
        print("{:10.3f}".format(flatteningPara(x, y, i)), end="")
        print("{:10.3f}".format(secondDerivative(y, 1, i)))
if __name__ == "__main__":
    main()
