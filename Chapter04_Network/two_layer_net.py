# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/1 21:22'
import numpy as np
from Chapter04_Network.functions import sigmoid, softmax, cross_enptropy_error
from Chapter04_Network.gradient import numerical_gradient


# (n_sample * features) * (input_size * hidden_size)
class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        # 初始化权重
        self.params = {}
        self.params["W1"] = weight_init_std * np.random.randn(input_size, hidden_size)
        self.params["b1"] = np.zeros(hidden_size).reshape(1, hidden_size)
        self.params["W2"] = weight_init_std * np.random.randn(hidden_size, output_size)
        self.params["b2"] = np.zeros(output_size).reshape(1, output_size)

    def predict(self, x):
        W1, W2 = self.params["W1"], self.params["W2"]
        b1, b2 = self.params["b1"], self.params["b2"]

        a1 = np.dot(x, W1) + b1
        z1 = sigmoid(a1)
        a2 = np.dot(z1, W2) + b2
        y = softmax(a2)
        return y

    def loss(self, x, t):
        """
        :param x:
        :param t:这里是标签，必须要进行one-hot编码
        :return:
        """
        y = self.predict(x)
        return cross_enptropy_error(y, t)

    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        t = np.argmax(t, axis=1)

        accuracy = np.sum(y == t) / float(x.shape[0])
        return accuracy

    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)

        grads = {}
        grads["W1"] = numerical_gradient(loss_W,self.params["W1"])
        grads["b1"] = numerical_gradient(loss_W,self.params["b1"])
        grads["W2"] = numerical_gradient(loss_W,self.params["W2"])
        grads["b2"] = numerical_gradient(loss_W,self.params["b2"])

        return grads

if __name__ == '__main__':
    net = TwoLayerNet(input_size=784,hidden_size=100,output_size=10)
    x = np.random.rand(100,784)
    y = net.predict(x)
    print(y)