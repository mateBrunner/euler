#!/usr/bin/python3.5
# triangular, pentagonal and hexagonal #45
import math

"""
def ispentagonal(szam):
    tort = (math.sqrt(1+24*szam)+1)/6
    return tort == int(tort)


def istriangular(szam):
    tort = (math.sqrt(1+8*szam)-1)/2
    return tort == int(tort)


def ishexagonal(szam):
    tort = (math.sqrt(1+8*szam)+1)/4
    return tort == int(tort)


talalat = 0
i = 0
while talalat < 4:
    i += 1
    szam = i*(2*i-1)
    if ispentagonal(szam) and istriangular(szam):
        talalat += 1
        print(szam) """


def generating_function():
    p3 = [1]
    p4 = []
    p5 = []
    p6 = []
    p7 = []
    p8 = []
    n = 2
    while len(str(p3[-1])) < 5:
        if len(str(n * (n + 1) / 2)) > 5:
            p3.append(int(n * (n + 1) / 2))
        if len(str(n ** 2)) > 3 and len(str(n ** 2)) < 5:
            p4.append(int(n ** 2))
        if len(str(n * (3 * n - 1) / 2)) > 5 and len(str(n * (3 * n - 1) / 2)) < 7:
            p5.append(int(n * (3 * n - 1) / 2))
        if len(str(n * (2 * n - 1))) > 3 and len(str(n * (2 * n - 1))) < 5:
            p6.append(int(n * (2 * n - 1)))
        if len(str(n * (5 * n - 3) / 2)) > 5 and len(str(n * (5 * n - 3) / 2)) < 7:
            p7.append(int(n * (5 * n - 3) / 2))
        if len(str(n * (3 * n - 2))) > 3 and len(str(n * (3 * n - 2))) < 5:
            p8.append(int(n * (3 * n - 2)))
        n += 1
    p3 = p3[1:-1]
    return p3, p4, p5, p6, p7, p8


p3, p4, p5, p6, p7, p8 = generating_function()
print(p3, p4, p5, p6, p7, p8)
