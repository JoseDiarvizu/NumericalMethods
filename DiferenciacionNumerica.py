# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 09:37:16 2020

@author: ESTEBAN
"""
import math
import sympy as sy
from sympy import *
from matplotlib import pyplot

x = sy.symbols('x')


def f(x):
    return x


def extremos(arr, fx, i):
    h = arr[1] - arr[0]
    if i > len(arr) / 2:
        h = -h
    if h > 0:
        return (-3 * fx[i] + 4 * fx[i + 1] - fx[i + 2]) / (2 * h)
    else:
        return (-3 * fx[i] + 4 * fx[i - 1] - fx[i - 2]) / (2 * h)


def extremos5(arr, fx, i):
    h = arr[1] - arr[0]
    if i > len(arr) / 2:
        h = -h
    if h > 0:
        return (-25 * fx[i] + 48 * fx[i + 1] - 36 * fx[i + 2] + 16 * fx[i + 3] - 3 * fx[i + 4]) / (12 * h)
    else:
        return (-25 * fx[i] + 48 * fx[i - 1] - 36 * fx[i - 2] + 16 * fx[i - 3] - 3 * fx[i - 4]) / (12 * h)


def centro(arr, fx, i):
    h = arr[1] - arr[0]
    # print("H",h,arr[i+cont],arr[i-1-cont])
    return (fx[i + 1] - fx[i - 1]) / (2 * h)


def centro5(arr, fx, i):
    h = arr[1] - arr[0]
    return ((fx[i - 2]) - 8 * fx[i - 1] + 8 * fx[i + 1] - fx[i + 2]) / (12 * h)


def fp(arr, fx, i):
    h = arr[1] - arr[0]
    return (fx[i - 1] - 2 * fx[i] + fx[i + 1]) / h ** 2


'''
pol=0
n=2
arr=[1,2,3]
fx=[2,4,6]
for i in range(n):
    div=1
    if i==0:
        a=sy.sympify(fx[i])
        for j in range(n):
            div=1
            if j!=i:
                b=sy.sympify(x-arr[j])
                div*=(arr[i]-arr[j])
                a=sy.sympify(a*(b/div))

                print(x-arr[j],arr[i],arr[j])
        pol=sy.sympify(g+a)
'''


def Dif(n, x, fx):
    h = x[1] - x[0]
    s = ""
    if n == 3:
        s += "     X        F(x)        F'(x)\n"
        s += str(" %.6f  " % x[0]) + " " + str(" %.6f  " % fx[0]) + " " + str(" %.6f  " % extremos(x, fx, 0)) + "\n"
        s += str(" %.6f  " % x[1]) + " " + str(" %.6f  " % fx[1]) + " " + str(" %.6f  " % centro(x, fx, 1)) + "\n"
        s += str(" %.6f  " % x[2]) + " " + str(" %.6f  " % fx[2]) + " " + str(" %.6f  " % extremos(x, fx, 2)) + "\n"
    # print(pol)   "f(x+h)-f(+)"
    #             -------------
    #                   h
    elif n == 5:
        s += "     X        F(x)       F'(x)       F''(x)\n"
        s += str(" %.6f  " % x[0]) + " " + str(" %.6f  " % fx[0]) + str(" %.6f  " % extremos5(x, fx, 0)) + "\n"
        s += str(" %.6f  " % x[1]) + " " + str(" %.6f  " % fx[1]) + str(" %.6f  " % centro(x, fx, 1)) + " " + str(
            " %.6f  " % fp(x, fx, 1)) + "\n"
        s += str(" %.6f  " % x[2]) + " " + str(" %.6f  " % fx[2]) + str(" %.6f  " % centro5(x, fx)) + " " + str(
            " %.6f  " % fp(x, fx, 2)) + "\n"
        s += str(" %.6f  " % x[3]) + " " + str(" %.6f  " % fx[3]) + str(" %.6f  " % centro(x, fx, 3)) + " " + str(
            " %.6f  " % fp(x, fx, 3)) + "\n"
        s += str(" %.6f  " % x[4]) + " " + str(" %.6f  " % fx[4]) + str(" %.6f  " % extremos5(x, fx, 4)) + "\n"
    return s


# print(Dif(5,[1.8,1.9,2,2.1,2.2],[10.889365,12.703199,14.778112,17.148957,19.85503]))

'''
x=[0.95,0.96,0.97,0.98,0.99,1]
fx=[0.90,1.92,2.54,2.88,3.04,3.10]
print("f(0.95):"," %.6f  "%extremos5(x,fx,0),"  R:"," %.6f  "%(extremos5(x,fx,0)*0.97+0.14*0))
print("f(0.96):"," %.6f  "%centro(x,fx,1),"  R:"," %.6f  "%(centro(x,fx,1)*0.97+0.14*1))
print("f(0.97):"," %.6f  "%centro5(x,fx,2),"  R:"," %.6f  "%(centro5(x,fx,2)*0.97+0.14*2))
print("f(0.98):"," %.6f  "%centro5(x,fx,3),"  R:"," %.6f  "%(centro5(x,fx,3)*0.97+0.14*3))
print("f(0.99):"," %.6f  "%centro(x,fx,4),"  R:"," %.6f  "%(centro(x,fx,4)*0.97+0.14*4))
print("f(1):"," %.6f  "%extremos5(x,fx,5),"  R:"," %.6f  "%(extremos5(x,fx,5)*0.97+0.14*5))
'''