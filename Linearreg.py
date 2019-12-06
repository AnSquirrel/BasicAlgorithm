
import numpy as np
import matplotlib.pyplot as plt

s = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11]]
space = np.array(s)
p = [[5.367], [5.376], [5.385], [5.433], [5.401], [5.381], [5.411], [5.418], [5.433], [5.439], [5.470]]
price = np.array(p)

def showfigure(x, y):
    plt.figure(figsize=(8, 6))
    plt.xlabel('HouseMonth')
    plt.ylabel('HousePrice')
    plt.plot(x, y, color='r', linewidth=2)
    plt.scatter(x, y, color='k', label='HomePrice', s=200)
    plt.legend()
    plt.show()

showfigure(space, price)


class LinearRegression(object):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def fit(self, x_train, y_train):
        x_train = np.array(x_train)
        y_train = np.array(y_train)

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        numer = denom = 0
        for x, y in zip(x_train, y_train):
            numer = numer + ((x - x_mean) * (y - y_mean))
            denom = denom + (x - x_mean) ** 2
        self.a = numer / denom
        self.b = y_mean - self.a * x_mean
        '''
        for i in range(len(x_train)):
            numer = np.sum([numer, (x_train[i] - x_mean) * (y_train[i] - y_mean)])
            denom = np.sum([denom, np.square(x_train[i] - x_mean)])
        self.a = numer / denom
        self.b = y_mean - self.a * x_mean
        '''
    def predict(self, x_test):
        y_pred = self.a * x_test + self.b
        return y_pred


LinearReg = LinearRegression()
LinearReg.fit(space, price)
y_pred = LinearReg.predict(space)
print(y_pred)

def show():
    plt.figure(figsize=(8, 6))
    plt.xlabel('HouseMonth')
    plt.ylabel('HousePrice')
    plt.scatter(space, price, color='k', s=200)
    plt.plot(space, y_pred, color='r', label='HomePrice', linewidth=3)
    plt.legend()
    plt.show()

show()

dec_price = LinearReg.predict(12)
print(dec_price)
