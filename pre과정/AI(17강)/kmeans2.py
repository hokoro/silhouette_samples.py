from sklearn.cluster import KMeans
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




km = KMeans(n_clusters=3,
            init = 'random',
            n_init = 10,
            max_iter= 300,
            tol = 1e-04,
            random_state=0)

'''
n_cluster: 클러스터의 개수 
init :기본 K평균 설정 
n_init:각기다른 랜던한 센트로이드에서 몇번 실행하여 가장 낮은 오차값을 쓸건디 
max_iter : 최대 몇번 반복하여 수행할것인지 
tol: 데이터 수치의 허용범위 해당범위를 넘어가면 종료 
random_state: 랜덤 시드값
'''
y_km = km.fit_predict(x)


plt.scatter(x[y_km == 0,0],
            x[y_km == 0,1],
            s = 50,c = 'lightgreen',
            marker = 's',edgecolors='black',
            label = 'cluster 1')
plt.scatter(x[y_km == 1,0],
            x[y_km == 1,1],
            s = 50,c = 'orange',
            marker = 'o',edgecolors='black',
            label = 'cluster 2')
plt.scatter(x[y_km == 2,0],
            x[y_km == 2,1],
            s = 50,c = 'lightblue',
            marker = 'v',edgecolors='black',
            label = 'cluster 3')
plt.scatter(km.cluster_centers_[:,0],
            km.cluster_centers_[:,1],
            s = 250,c = 'red',
            marker = '*',edgecolors='black',
            label = 'centroids')

plt.legend(scatterpoints = 1)

plt.grid()
plt.tight_layout()
plt.show()



#랜덤 하게 스타트 하는 위치 때문에 힘들다
