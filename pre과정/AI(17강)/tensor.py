import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
"""
모델링의 순서는
입력 x  ----------> 활성화 함수 f(x) --------> 출력
       가중치 w

y = f(x * w)


"""

import tensorflow as tf
import math


def sigmoid(x): #대표적인 활성화 함수
    return 1 / (1 + math.exp(-x))


tf.compat.v1.set_random_seed(2020) #게산 할때 마다 새로운 난수를 생성하는 코드
x = 1
y = 0
w = tf.random.normal([1], 0, 1)
b = tf.random.normal([1],0,1)
'''
[1] : w의 tensor 의 모양 
 0: 평균 
 1: 표준편차 
'''
#print(w)
output = sigmoid(x * w) #활성화 함수를 적용하기전에 x와 w 가중치를 곱해주어야 한다.
print(output) #0.474 but 우리가 원하는 출력값은 0 이기떄문에 오차가  0 - 0.474 정도 차이가 나는 것을 알수있다.

for i in range(1000):
    output = sigmoid(x*w+1*b)
    error = y - output #실제 결과값에서 학습한 결과 값으로 빼주는 것이다.
    w = w+x*0.1* error
    b = b+1*0.1*error
    '''
    0.1 은 학습률
    만약 x 가 0 이 되버리면 학습률 인 0.1 과 곱해도 계속 0만 뜨는 결과가 발생하기 떄문에
    가중치 변화가 안일어 난다.
    이를 방지하기 위해 편향 이라는 개념이 도입되는데 
    이는 입력으로는 늘 한쪽으로 치우처진 고정값이다 
    학습을 못하는 경우를 방지 해준다 
    '''
    if i %100 == 99:
        print("학습횟수:",i,"Error:",error,"예측 결과:",output)
