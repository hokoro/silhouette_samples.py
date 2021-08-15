import os
import numpy as np
import tensorflow as tf
import math
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'



def sigmoid(x): #대표적인 활성화 함수
    return 1 / (1 + math.exp(-x))
x = np.array([[1,1],[1,0],[0,1],[0,0]])
y = np.array([[0],[1],[1],[1]])
w = tf.random.normal([2],0,1)
b = tf.random.normal([1],0,1)
b_x = 1
for i in range(2000):
    error_sum = 0
    for j in range(4):
        output = sigmoid(np.sum(x[j]*w)+b_x*b)
        error = y[j][0] - output
        w = w + x[j] * 0.1 *error
        b = b + b_x *0.1 *error
        error_sum +=error


for i in range(4):
    print('X:',x[i],'Y:',y[i],'Output:',sigmoid(np.sum(x[i]*w)+b))

'''
X: [1 1] Y: [0] Output: 0.03543595136626948
X: [1 0] Y: [1] Output: 0.9748905393856805
X: [0 1] Y: [1] Output: 0.9748131047583647
X: [0 0] Y: [1] Output: 0.9999755523447257
'''