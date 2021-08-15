#1.모든 데이터의 거리 행렬을 계산합니다.
import numpy as np
import pandas as pd
np.random.seed(123)
x = np.random.random_sample([5,3])*10
print(x) #5x3 랜덤 행렬 데이터를 10 배 해서 저장

variables = ['X','Y','Z']
labels = ['ID_0','ID_1','ID_2','ID_3','ID_4']

df = pd.DataFrame(x,columns = variables,index = labels) #columns = 세로 index = 가로
print(df)


#2.모든 데이터를 단일 클러스터로 표현 거리행렬을 계산하기 위해
from scipy.spatial.distance import pdist , squareform
y = pdist(df) #축약된 거리 행렬 계산
print(y)

row_dist = pd.DataFrame(squareform(pdist(df,metric = 'euclidean')),columns = labels,index = labels) #squareform 거리 행렬 벡터를 행렬 형식으로 변환
from scipy.cluster.hierarchy import linkage
row_clusters = linkage(row_dist,
                       method = 'complete',
                       metric = 'euclidean')
#초기 데이터 배열을 전달하고 euclidean 지표를 매개변수로 사용한다.

#help(linkage)
print(row_clusters)
row_clusters = linkage(pdist(df,metric = 'euclidean'),method = 'complete')
print(row_clusters)
row_clusters = linkage(df.values,method = 'complete',metric = 'euclidean')
print(row_clusters)


#군집 결과를 자세히 볼려면 pandas DataFrame 에 넣고 출력해주면 된다,
a = pd.DataFrame(row_clusters,
             columns = ['row label 1', 'row label 2','distance','no. of items in clust.'],
             index = ['cluster %d' %(i+1) for i in range(row_clusters.shape[0])])
print(a)

import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
row_dendr = dendrogram(row_clusters,
                       labels = labels)
plt.tight_layout()
plt.ylabel('Euclidean distance')
plt.show()