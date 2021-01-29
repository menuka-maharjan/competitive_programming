#!/bin/python3

import sys
import math

def lowestTriangle(base, area):
    x=math.ceil((2*area)/base)
    return x
    # Complete this function

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
