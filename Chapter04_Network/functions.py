# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/2 9:12'
import numpy as np
def is_leap(x):
    return ((x % 4 == 0) and (x % 100 != 0)) or (x % 400 == 0)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a- c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def cross_enptropy_error(y,t):
    delta = 1e-7
    if y.dim == 1:
        t = t.reshape(1,t.size)
        y = y.reshape(1,y.size)
    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + delta)) / batch_size