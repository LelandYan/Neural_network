# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/6 16:34'
import numpy as np
import pandas as pd

data = pd.read_csv(r"E:\problem_b\train_set1.csv",encoding="gbk")
data_label = ["ip","app"]
print(data.head())