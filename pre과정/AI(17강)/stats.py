#통계학 데이터 사용해 보기
import numpy as np
from scipy import stats

#랜덤 함수를 사용
np.random.seed(0)

#랜덤하게 0~100 사이의 데이터를 10000개만 만들기
#data_A = np.random.randint(0,100,10000)
data_B= np.random.normal(size = 100) #정규 분포로 만들어서 보여주기


#평균 중앙값 최빈값 저장
mean = np.mean(data_B) #평균
median = np.median(data_B) #중앙값
mode = stats.mode(data_B)#최빈값

print("평균:",mean.round(2))  # 소수 두번째 자리까지 출력
print("중앙값:",median) # 중앙 값을 출력
print("최빈값: {} ( {} )".format(mode[0][0],mode[1][0])) #해당수 , 빈도 출력  을 format 기법을 사용해서 출력

