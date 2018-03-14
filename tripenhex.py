#!/usr/bin/python3.5
# cyclical figurate numbers #61
import math





listak = [p3,p4,p5,p6,p7,p8]
kilove = [0]

def ciklusos(szam1,szam2):
    if str(szam1[3:]) == str(szam2[:2]):
        return True
    return False

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
