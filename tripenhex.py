#!/usr/bin/python3.5
# cyclical figurate numbers #61
import math

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



listak = [p3,p4,p5]
kilove = [0]

def ciklusos(szam1,szam2):
    if str(szam1)[3:] == str(szam2)[:2]:
        return True
    return False

for i3 in listak[0]:
    for n1 in range(1,3):
        if n1 not in kilove:
            for i4 in listak[n1]:
                if ciklusos(i3,i4):
                    kilove.append(n1)
                    for n2 in range(1,3):
                        if n2 not in kilove:
                            for i5 in listak[n2]:
                                if ciklusos(i4,i5):
                                    kilove.append(n2)
                                    print(i3,i4,i5)
                        if n2 in kilove: kilove.remove(n1)
        if n1 in kilove: kilove.remove(n1)
                    
"""
for i3 in listak[0]:
    for n1 in range(1,6):
        if n1 not in kilove:
            for i4 in listak[n1]:
                if ciklusos(i3,i4):
                    kilove.append(n1)
                    for n2 in range(1,6):
                        if n2 not in kilove:
                            for i5 in listak[n2]:
                                if ciklusos(i4,i5):
                                    kilove.append(n2)

                                    for n2 in range(1,6):
                                        if n2 not in kilove:
                                            for i5 in listak[n2]:
                                                if ciklusos(i4,i5):
                                                    kilove.append(n2)

                                                    for n2 in range(1,6):
                                                        if n2 not in kilove:
                                                            for i5 in listak[n2]:
                                                                if ciklusos(i4,i5):
                                                                    kilove.append(n2)

                                                                    for n2 in range(1,6):
                                                                        if n2 not in kilove:
                                                                            for i5 in listak[n2]:
                                                                                if ciklusos(i4,i5):
                                                                                    kilove.append(n2)



                        if n2 in kilove: kilove.remove(n1)
        if n1 in kilove: kilove.remove(n1)

"""


