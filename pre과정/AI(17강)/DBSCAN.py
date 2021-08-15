from sklearn.metrics import silhouette_samples
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#군집이 잘 잡힌경우 실루엣 계수가 1에 가까운 수준이다.
#무작위 데이터 셋을 생성할수가 있음
x,y = make_blobs(n_samples=150,n_features=2,centers = 3,cluster_std=0.5,shuffle=True,random_state=0)
km = KMeans(n_clusters=3,
            init = 'random',
            n_init = 10,
            max_iter= 300,
            tol = 1e-04,
            random_state=0)
y_km = km.fit_predict(x)
#print(y_km) #y_km 은 3개의 클러스터 가 한종류씩 배당 되기 떄문에  0,1,2
cluster_labels = np.unique(y_km) #unquie() : 배열의 중복된 원소를 제거루 유일한 원소를 정렬하여 반환
n_clusters = cluster_labels.shape[0] #shape 값은 3

#print(cluster_labels) #중복을 뺏으니 0,1,2 만 나옴

#x : 임의의 데이터 셋 y_km: 예측 클래스 에 대한 계체 metric : 거리측정방식
silhouette_vals = silhouette_samples(x,y_km,metric='euclidean')

y_ax_lower,y_ax_upper = 0,0
yticks = []
for i,c in enumerate(cluster_labels):
    c_silhouette_vals = silhouette_vals[y_km == c]
    c_silhouette_vals.sort() #클러스에 맞는 원소들을 정렬
    #print(i,c_silhouette_vals)

    y_ax_upper += len(c_silhouette_vals)

    color = cm.jet(float(i)/n_clusters) #색깔을 설정할수있는 matplot method
    #jet 의특징은 밝은 하늘색에서 연두색 까지 그 사이값만 표현을 한다.

    plt.barh(range(y_ax_lower,y_ax_upper),c_silhouette_vals,height=1.0,edgecolor = 'none',color = color)
    yticks.append((y_ax_lower+y_ax_upper)/2.)
    y_ax_lower += len(c_silhouette_vals)

silhouette_avg = np.mean(silhouette_vals)
plt.axvline(silhouette_avg,color = 'red',linestyle = "--") #데이터의 평균 라인을 그리고 싶을떄 쓰는 함수

plt.yticks(yticks,cluster_labels+1)  #눈금 표시하는 함수
plt.ylabel("cluster")
plt.xlabel("silhouette coefficient")

plt.tight_layout()
plt.show()

#밀집도 기반 군집을 구현해보자
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
x,y = make_moons(n_samples = 200,
                 noise = 0.05, #잡음의크기 0이되면 정확하게 반달을 이룬다.
                 random_state = 0)


plt.scatter(x[:,0],x[:,1])
plt.tight_layout()
plt.show()

from sklearn.cluster import AgglomerativeClustering
f,(ax1,ax2) = plt.subplots(1,2,figsize = (8,3))
km = KMeans(n_clusters = 2,random_state = 0)
y_km = km.fit_predict(x)
ax1.scatter(x[y_km==0,0],x[y_km == 0,1],
            edgecolor = 'black',
            c = 'lightblue',marker = 'o',s = 40,label = 'cluster 1')
ax1.scatter(x[y_km == 1,0],x[y_km == 1,1],
            edgecolor = 'black',c = 'red',marker = 's',s = 40,label = 'cluster 2')
ax1.set_title('K-means clustering')

ac = AgglomerativeClustering(n_clusters = 2,affinity = 'euclidean',linkage ='complete')

y_ac = ac.fit_predict(x)
ax2.scatter(x[y_ac ==0,0],x[y_ac == 0,1],c = 'lightblue',edgecolor = 'black',marker = 'o',s= 40,label = 'cluster 1')
ax2.scatter(x[y_ac == 1,0],x[y_ac == 1,1],c = 'red',edgecolor = 'black',marker = 's',s = 40,label = 'cluster 2')
ax2.set_title('Agglomerative clustering')

plt.legend()
plt.tight_layout()
plt.show()

#밀집도 기반 알고리즘 분석
from sklearn.cluster import DBSCAN
db = DBSCAN(eps = 0.2 , min_samples = 5,metric = 'euclidean')
'''
eps : 엡실론 영역
min sample : 최소 개수 
metric: 데이터 분류 기준 
엡실론과 최소 샘플의수가 가장 중요 하다.
'''
y_db = db.fit_predict(x)

plt.scatter(x[y_db ==0,0],x[y_db == 0,1],c = 'lightblue',marker = 'o',s = 40,edgecolors= 'black',label = 'cluster 1')
plt.scatter(x[y_db == 1,0],x[y_db == 1,1],c = 'red',marker = 's',s = 40,edgecolors= 'black',label = 'cluster 2')
plt.legend()
plt.tight_layout()
plt.show()

