from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

#무작위 데이터 셋을 생성할수가 있음
x,y = make_blobs(n_samples=150,n_features=2,centers = 3,cluster_std=0.5,shuffle=True,random_state=0)

distortions = []
for i in range(1,11):
    km = KMeans(n_clusters=i,
                init = 'k-means++',
                n_init = 10,
                max_iter= 300,
                tol = 1e-04,
                random_state= 0)
    km.fit(x)
    print("왜곡 : %.2f" % km.inertia_)
    distortions.append(km.inertia_)

plt.plot(range(1,11),distortions,marker = 'o')
plt.xlabel('number of clusters')
plt.ylabel('Distortion')
plt.tight_layout()
plt.show()

#k 가 늘어날때 마다 왜곡 값이 줄어들었다
#위에 기번은
'''
초기 센트로이드를 멀리 떨어트리도록 위치 시키는것이다. 
왜곡 : 713.70
왜곡 : 283.46
왜곡 : 72.48
왜곡 : 62.84
왜곡 : 53.87
왜곡 : 47.04
왜곡 : 41.19
왜곡 : 35.41
왜곡 : 30.25
왜곡 : 27.77

왜곡 값이 줄어드는것을 확인 
'''

#왜곡 수치 확인하기 km.inertia_
