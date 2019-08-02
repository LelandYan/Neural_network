# _*_ coding: utf-8 _*_
__author__ = 'LelandYan'
__date__ = '2019/8/2 10:52'

class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self,x,y):
        self.x = x
        self.y = y
        out = x * y

        return out

    def backward(self,dout):
        dx = dout * self.y
        dy = dout * self.x

        return dx,dy

class AddLayer:
    def __init__(self):
        pass

    def forward(self,x,y):
        out = x + y
        return out

    def backward(self,dout):
        dx = dout * 1
        dy = dout * 1
        return dx,dy



if __name__ == '__main__':
    apple = 100
    apple_num = 2
    tax = 1.1

    mul_apple_layer = MulLayer()
    mul_tax_layer = MulLayer()

    apple_price = mul_apple_layer.forward(apple,apple_num)
    price = mul_tax_layer.forward(apple_price,tax)

    print(price)

    dprice = 1
    dapple_price,dtax = mul_tax_layer.backward(dprice)
    dapple,dapple_num = mul_apple_layer.backward(dapple_price)