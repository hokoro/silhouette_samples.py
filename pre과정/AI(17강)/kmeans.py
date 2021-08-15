from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

#무작위 데이터 셋을 생성할수가 있음
x,y = make_blobs(n_samples=150,n_features=2,centers = 3,cluster_std=0.5,shuffle=True,random_state=0)

'''
make_blobs 의 매개변수 옵션 
n_sample:샘플의 수 
n_features: 차원수 = 특성수 
center : 클러스터 분리 개수 
cluster_std: 분산 
shuffle: 데이터를 섞을건지 정함
random_state : 랜덤 시드값
'''

#matplotlib 를 이용해 2차원 산점도 를 그리는것이 목표
#+ 특성의 유사도에 기초하여 데이터들을 그룹으로 모으는것 이다.
plt.scatter(x[:,0],
            x[:,1],
            c= 'white',
            marker = 'o',
            edgecolors= 'black',
            s = 50)
plt.grid()
plt.tight_layout()
plt.show()
