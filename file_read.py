from numpy import *
import matplotlib.pyplot as plt
import numpy as np
# read the time series data from file
def txtinput(path, a):
    X = []
    with open(str(path), 'r') as f:
        lines = f.readlines()
        for line in lines:
            value = [float(s) for s in line.split()]
            X.append(value[a])
    return X

def txtinput_c(path):
    X = []
    with open(str(path), 'r') as f:
        lines = f.readlines()
        for line in lines:
            value = [float(s) for s in line.split()]
            X.append(value)
    return X
