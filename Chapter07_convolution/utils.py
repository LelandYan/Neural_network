# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/2 15:45'
import numpy as np


def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
    """
    :param input_data: 由（数据量，通道，高，长）的4维数组构成的输入数据
    :param filter_h: 过滤器的高
    :param filter_w: 过滤器的长
    :param stride: 步幅
    :param pad: 填充
    :return: 2 维数组
    """
    N, C, H, W = input_data.shape
    out_h = (H + 2 * pad - filter_h) // stride + 1
    out_w = (W + 2 * pad - filter_w) // stride + 1

    img = np.pad(input_data, [(0, 0), (0, 0), (pad, pad), (pad, pad)], "constant")
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

    for y in range(filter_h):
        y_max = y + stride * out_h
        for x in range(filter_w):
            x_max = x + stride * out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]
    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N * out_h * out_w, -1)
    return col
