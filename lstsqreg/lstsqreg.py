# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def leastSquaresRegressor(A, b):
    B = np.matmul(np.transpose(A), A)
    c = np.matmul(np.transpose(A), b)
    x = np.linalg.solve(B, c)
    return x, np.linalg.norm(A*x[:] - b[:])
A = np.array([[1, 1], [1, 3], [1, 5], [1, 7]])
b = np.array([14, 17, 19, 20])

x, res = leastSquaresRegressor(A, b)

