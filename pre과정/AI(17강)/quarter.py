import numpy as np #numberpython
from scipy import stats #통계학 라이브러리

#무작위 난수 설정 = 같은 무작위 공간을 설정
np.random.seed(0)

#data_A 에 랜덤으로 (0~100) 까지의 수중에 1만개의 데이터 저장
data_A = np.random.randint(0,100,10000)
#데이터 타입: numpy 데이터 수 : 1만개
print(type(data_A))
print(data_A)

#평균 중앙 최빈값
mean = np.mean(data_A) #mean =평균
median = np.median(data_A) #median = 중앙
mode = stats.mode(data_A) #mode =최빈값


print("평균값 : ",mean.round(2)) #round(num) : 소수점 처리
print("중앙값 : ",median)
print("최빈값 : {} ( {} )".format(mode[0][0],mode[1][0]))

#mode[0][0] : 해당수 , mode[1][0] : 빈도수
#표준편차,분산

data_A_var = np.var(data_A)
data_A_std = np.std(data_A)

#분산값으로 비교할려며 크기 때문에 쉽지 않아서 표준편차 해야하는것이다.
print("분산 : ",data_A_var.round(2)) #분산 : 편차 제곱의 평균
print("표준편차 : ",data_A_std.round(2)) #표준편차 : 편차 제곱의 평균 제곱근

#사분위수
import pandas as pd

A = pd.Series([20,21,23,22,26,28,35,35,41,42,43,45,44,45,46,47,47,46,47,58,58,59,60,56,57,57,80])
B = pd.Series([5,6,11,13,15,16,20,20,21,23,22,27,27,30,30,32,36,37,37,40,40,43,44,45,51,54,70])

A_Q1 = A.quantile(0.25) ; print("1사분위수 : ",A_Q1)
A_Q2 = A.quantile(0.5) ; print("2사분위수 : ",A_Q2)
A_Q3 = A.quantile(0.75) ; print("3사분위수 : ",A_Q3)
A_Q4 = A.quantile(1) ; print("4사분위수 : ",A_Q4,'\n')

B_Q1 = B.quantile(0.25) ; print("1사분위수 : ",B_Q1)
B_Q2 = B.quantile(0.5) ; print("2사분위수 : ",B_Q2)
B_Q3 = B.quantile(0.75) ; print("3사분위수 : ",B_Q3)
B_Q4 = B.quantile(1) ; print("4사분위수 : ",B_Q4,'\n')
'''
1사분위수 :  35.0
2사분위수 :  45.0
3사분위수 :  56.5 50분 이네 배달 
4사분위수 :  80.0 

1사분위수 :  20.0
2사분위수 :  30.0
3사분위수 :  40.75  40분 이네 배달
4사분위수 :  600.0 
'''

#박스 플롯으로 4분위수 보기
import matplotlib.pyplot as plt

plt.boxplot((A,B))

'''
박스 위 아래의 점은 이상치를 제외한 최댓값 최솟값
박스에 선 부분은 Q2 
박스에 위 아래는 각각 3사분위, 1사분위 수 
'''

plt.grid()
plt.show()

#IQR 사분범위에 1.5배 기준으로 산정
#IQR = Q3 - Q1

IQR = A_Q3 - A_Q1
print("IQR : ", IQR)
Step1 = IQR * 1.5 #step1 : 첫번쨰 사분범위 에서 1.5를 곱해준다
print("Step1 : ",Step1)

#하단 이상치 기준선은 1사분위수에서 사분범위의 1.5배 값을 빼준다음 이값을 기준으로 이값보다 작으면 이상치로 간주

Lower_fence = A_Q1 - Step1
print(Lower_fence)

#상단 이상치 기준선

Upper_fence = A_Q3 + Step1
print(Upper_fence)


