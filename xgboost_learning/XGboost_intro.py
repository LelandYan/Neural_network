# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/6 18:32'
import numpy as np
import xgboost as xgb

if __name__ == '__main__':
    # 读取数据
    data_train = xgb.DMatrix("12.agaricus_train.txt")
    data_test = xgb.DMatrix("12.agaricus_test.txt")

    # 设置参数
    param = {"max_depth":2,"eta":1,"silent":1,"objective":"binary:logitraw"}

    watchlist = [(data_test,"eval"),(data_train,"train")]
    n_round = 3
    bst = xgb.train(param,data_train,num_boost_round=n_round,evals=watchlist)

    # 计算错误率
    y_hat = bst.predict(data_test)
    y = data_test.get_label()
    print(y_hat)
    print(y)
    error = sum(y != (y_hat > 0))
    error_rate = float(error) / len(y_hat)
    print('样本总数：\t', len(y_hat))
    print('错误数目：\t%4d' % error)
    print('错误率：\t%.5f%%' % (100 * error_rate))












