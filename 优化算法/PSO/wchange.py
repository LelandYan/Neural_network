# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/5 18:40'
import numpy as np
import matplotlib.pyplot as plt

ws = 0.9
we = 0.4
max_gen = 300

w = [0 for _ in range(max_gen)]
for k in range(max_gen):
    w[k] = ws - (ws - we) * (k / max_gen)

plt.plot(np.arange(max_gen), w,label="Relu-1")

for k in range(max_gen):
    w[k] = ws - (ws - we) * (k / max_gen) ** 2

plt.plot(np.arange(max_gen), w,label="Relu-2")

for k in range(max_gen):
    w[k] = ws - (ws - we) * (2 * k / max_gen - (k / max_gen) ** 2)

plt.plot(np.arange(max_gen), w,label="Relu-3")

for k in range(max_gen):
    w[k] = we * (ws / we) ** (1 / (1 + 10 * k / max_gen))
plt.plot(np.arange(max_gen), w,label="Relu-4")

plt.legend()
plt.show()